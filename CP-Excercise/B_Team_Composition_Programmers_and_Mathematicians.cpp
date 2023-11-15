#include<bits/stdc++.h>
using namespace std;
using ll=long long int;
#define MOD 10^9+7

void solve(){
	ll a,b;
	cin>>a>>b;
	ll mn=min(a,b);
    ll low=0;
    ll high=mn;
    ll ans=0;
    while(low<=high)
    {
        ll mid=low+(high-low)/2;
        cout<<"m "<<mid<<endl;
        if((a-mid)+(b-mid) >=2*mid)
        {
            ans=mid;
            low=mid+1;
        }
        else  
        {
            high=mid-1;
        }
        cout<<low<<" "<<high<<endl;
    }
    cout<<ans;
	
}

int main(){
	ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
	ll t;
	cin>>t;
	while(t--){
		solve();
		cout<<endl;
	}
	//solve()
	return 0;
}
