#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define MOD 1000000007
#define SIZE le6+2
#define endl "\n"

void solve(){
ll n; cin>>n;
vector<ll>a(n);
for(ll i=0; i<n; i++) cin>>a[i];
bool flag = true;
for(ll i = n-1;i>0;i-=2)
{
if(a[i]<a[i-1])
{
if(i-1==0) flag = false;
else a[i-2]-=(a[i-1]-a[i]);
}
else if(i-2>=0) a[i-2]+=(a[i]-a[i-1]);
}
if(flag) cout<<"YES"<<endl;
else cout<<"NO"<<endl;

}

int main(){

ll t; cin>>t;
while(t--){
solve();
}
}