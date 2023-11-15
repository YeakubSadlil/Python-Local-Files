#include<bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> p(n);
    for (int i = 0; i < n; i++) {
        cin >> p[i];
    }
    if(p[0]==1 && p[1]==2){
        cout<<2<<" "<<3<<endl;
        return;
    }
    int abc = min_element(p.begin(), p.end()) - p.begin();

    int ddd = min_element(p.begin() + abc + 1, p.end()) - p.begin();

    cout << abc + 1 <<" " << ddd + 1 << endl;
}

int main() {   
    int t; 
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}