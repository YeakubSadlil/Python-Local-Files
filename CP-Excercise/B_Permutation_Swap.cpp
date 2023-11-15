#include <bits/stdc++.h>
using namespace std;
#define fast ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define ll long long int
#define ull unsigned long long int
#define pb push_back
vector < int > adj[10001]; 
bool g[10001][10001]; 
int color[10001]; 
const int MAXN = 105; 
ull t; 
int main() { 
fast; 
cin >> t; 
while (t--)
    {
        ll n; 
        cin>>n;
        vector< int > a(n); 
        map<ll,ll> m1,m2,m3; 
        for(int i = 0; i < n; i++) 
        { 
            cin>>a[i];
            m1[a[i]]=i+1;
        }
        
        for(int i = 0; i < n; i++)
        { 
            m2[i+1]=i+1; 
        } 
        ll cnt=0, ans=0;
        for(int i = 0; i < n; i++) 
        { 
            m3[abs(m1[i+1]-m2[i+1])]++;
            
        } 
        ll gcd; 
        for(auto x: m3) 
        { //gcd=__gcd() 
            gcd=x.first; 
            break; 
        }
        for(auto x: m3) 
        gcd=__gcd(gcd,x.first); 
        cout<<gcd<<endl;
    } 
    return 0; 
}
