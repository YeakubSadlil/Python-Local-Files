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
const int MOD = 1e9 + 7; 
int main()
{
    fast; 
    cin>> t;
    while (t--)
    { 
        ll n;
        cin >> n;
        vector < long long > a(n) , b(n);
        for(ll i = 0; i < n; i++) 
        { 
            cin >> a[i]; 
        } 
        for(ll i = 0; i < n; i++)
        {
            cin >> b[i];
            
        }
        sort(a.begin() , a.end()); 
        sort(b.begin() , b.end());
        reverse(a.begin() , a.end());
        reverse(b.begin() , b.end()); 
        ll j = 0, ans = 1;
        for (ll i = 0; i < n; i++)
        {
            while (j < n && a[i] <= b[j]) j++;
            ans = (ans * (i-j+1LL)) % MOD;
        }
cout << ans << endl; 
    }
return 0; 
}
