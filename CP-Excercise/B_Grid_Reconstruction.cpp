#include<bits/stdc++.h>
using namespace std;
#define vll vector<long long>
void solve()
{
    long long i,j,k,n,m;
    cin>>n;
    vector<vll>ans(2,vll(n));

    long long mx=2*n;

    ans[0][0]=mx;
    ans[1][n-1]=mx-1;

    long long front=1;
    long long back=mx-2;
    for(i=0;i<n-1;i++)
    {
        if(i&1)
        {
            ans[1][i]=back-1;
            ans[0][i+1]=back;
            back-=2;

        }

        else
        {
            ans[1][i]=front;
            ans[0][i+1]=front+1;
            front+=2;
        }
}

for(i=0;i<2;i++)
{
    for(j=0;j<n; j++)
        {
            cout<<ans[i][j]<<" ";
        }
        cout<<endl;
}
}
int main(){
long long t; cin>>t;
    while(t--)
    {
        solve();
    }
    return 0;
}