#include <bits/stdc++.h>
using namespace std;

const int mx = 9e5 + 10;
typedef long long ll;

ll l,r,mid,n,abc;
bool visited[mx] , gos[mx];
ll tmp[mx];
vector<int> g[mx];

void dfs(ll var , ll j = -1){
    if (g[var].size()==1 && var!=1) tmp[var] = 1;
    for (auto v:g[var]){
        if (v!=j) {
            dfs(v,var);
            tmp[var] += tmp[v];
        }
    }
}

int main(){
    ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);
    int t;
    cin >> t;
    while (t--){
        cin >> n;
        for (int i=1; i<=n; i++) {
            g[i].clear();
            tmp[i] = 0;
        }
        for (int i=1; i<n; i++){
            cin >> l >> r;
            g[l].push_back(r);
            g[r].push_back(l);
        }
        dfs(1);

        cin >> abc;
        vector<ll> store;
        while (abc--){
            cin >> l >> r;
            store.push_back(tmp[l] * tmp[r]);
        }

        for (int i = 0; i < store.size(); i++) {
            cout << store[i] << endl;
        }
    }
    return 0;
}
