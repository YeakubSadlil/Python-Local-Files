#include <bits/stdc++.h>
using namespace std;
#define ll long long


const int MAXN = 105;

void solve()

{

    int n;
    cin >> n;
    vector < int > a(n + 1) , b(n + 1);
    map< int , vector < int > > mp;
    for(int i = 1; i <= n; i++)
    {
        cin >> a[i] >> b[i];
        mp[a[i]].emplace_back(b[i]);
    }
    for(int i = 1; i <= n; i++)
    {
        sort(mp[i].begin() , mp[i].end() , greater<int>());
    }
    long long cem = 0;
    for(int i = 1; i <= n; i++)
    {
        for(int j = 0; j < i && j < mp[i].size(); j++)
        {
            cem += mp[i][j];
        }
    }

    cout << cem << endl;
}

int main()
{
    int t;
    cin >> t;
    while(t--)
    {
        solve();
    }
}   
