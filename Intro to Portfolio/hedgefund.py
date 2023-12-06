import pandas as pd
import scipy.stats
import numpy as np
from scipy.stats import norm
from scipy.optimize import minimize

def get_hfi_returns():
    hfi = pd.read_csv("data/edhec-hedgefundindices.csv",header=0,index_col=0,parse_dates=True)
    hfi = hfi/100
    hfi.index = hfi.index.to_period("M")
    return hfi

def get_ind_returns():
    ind = pd.read_csv("data/ind30_m_vw_rets.csv",header=0,index_col=0,parse_dates=True)
    ind.index = pd.to_datetime(ind.index, format="%Y%m").to_period("M")
    ind.columns = ind.columns.str.strip()
    return ind

def get_ind_size():
    ind = pd.read_csv("data/ind30_m_size.csv",header=0,index_col=0,parse_dates=True)
    ind.index = pd.to_datetime(ind.index, format="%Y%m").to_period("M")
    ind.columns = ind.columns.str.strip()
    return ind

def get_ind_nfirms():
    ind = pd.read_csv("data/ind30_m_nfirms.csv",header=0,index_col=0,parse_dates=True)
    ind.index = pd.to_datetime(ind.index, format="%Y%m").to_period("M")
    ind.columns = ind.columns.str.strip()
    return ind

def drawdownfunc(return_series: pd.Series):
    wealth_index = 1000*(1+return_series).cumprod()
    previous_peak = wealth_index.cummax()
    drawdown = (wealth_index-previous_peak)/previous_peak
    return pd.DataFrame(
    {
        "Wealth":wealth_index,
        "Peaks": previous_peak,
        "Drawdown":drawdown
    })

def skewness(r):
    demeaned_r = r - r.mean()
    sigma_r = r.std(ddof=0)
    exp = (demeaned_r**3).mean()
    return exp/sigma_r**3

def kartosis(r):
    demeaned_r = r - r.mean()
    sigma_r = r.std(ddof=0)
    exp = (demeaned_r**4).mean()
    return exp/sigma_r**4


def is_normal(r,level=0.01):
    res = scipy.stats.jarque_bera(r)
    return res[1]>level

def semideviation(r):
    return r[r<0].std(ddof=0)

def cvar_historic(r,level=5):
    if isinstance(r,pd.Series):
        is_beyond = r <= -var_historic(r,level=level)
        return -r[is_beyond].mean()
    elif isinstance(r, pd.DataFrame):
        return r.aggregate(cvar_historic, level=level)
    else:
        raise TypeError("Expected to be series or dataframe")
        

def var_gaussian(r,level=5):
    z = norm.ppf(level/100)
    return -(r.mean()+z*r.std(ddof=0))

def var_historic(r,level=5):
    if isinstance(r,pd.DataFrame):
        return r.aggregate(var_historic, level=level)
    elif isinstance(r, pd.Series):
        return -np.percentile(r,level)
    else:
        raise TypeError("Expected to be series or dataframe")
        
def annualized_vol(r,periods_per_year):
    return r.std()*(periods_per_year**0.5)

def annualized_ret(r,periods_per_year):
    compounded_growth = (1+r).prod()
    return compounded_growth**(periods_per_year/r.shape[0]) -1

def sharp_ratio(r,risk_free_rate,periods_per_year):
    rf_per_period = (1+risk_free_rate)**(1/periods_per_year)-1
    excess_return = r - rf_per_period
    ann_excess_return = annualized_ret(excess_return,periods_per_year)
    anno_vol  = annualized_vol(r,periods_per_year)
    return ann_excess_return/anno_vol
    
    
def portfolio_return(weights,returns):
    """
    Weights -> Returns
    """
    return weights.T @ returns

def portfolio_vol(weights,covmat):
    """
    Weights -> Volatility
    """
    return (weights.T @ covmat @ weights)**0.5

def plot_ef2(n_points,er,cov,style="-."):
    weights = [np.array([w,1-w]) for w in np.linspace(0,1,n_points)]
    rets = [portfolio_return(w,er) for w in weights]
    vol  = [portfolio_vol(w,cov) for w in weights]
    ef = pd.DataFrame(
    {
        "Returns": rets,
        "Volatility": vol
    })
    return ef.plot.line(x="Volatility",y="Returns", style=style)

def plot_ef(n_points,er,cov,style="-."):
    weights = minimize_vol(target_return)
    rets = [portfolio_return(w,er) for w in weights]
    vol  = [portfolio_vol(w,cov) for w in weights]
    ef = pd.DataFrame(
    {
        "Returns": rets,
        "Volatility": vols
    })
    return ef.plot.line(x="Volatility",y="Returns", style=style)

def minimize_vol(target_return,er,cov):
    """
    target_return -> weights
    """
    n = er.shape[0]
    init_guess = np.repeat(1/n,n)
    bounds = ((0.0,1.0),)*n
    return_is_target = {
        'type':'eq',
        'args': (er,),
        'fun' : lambda weights, er: target_return - portfolio_return(weights,er)
    }
    weights_sum_to_1 ={
        'type':'eq',
        'fun' : lambda weights: np.sum(weights) -1 
    }
        
    results = minimize(portfolio_vol,init_guess,
                      args=(cov,), method="SLSQP",
                      options={'disp':False},
                      constraints=(return_is_target,weights_sum_to_1),
                       bounds=bounds
                      )
    return results.x