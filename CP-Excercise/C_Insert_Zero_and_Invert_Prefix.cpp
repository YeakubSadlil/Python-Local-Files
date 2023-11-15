#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    vector<int> a(n);
    for(int i= 0; i < n; i++) {
    cin >> a[i];
    }


    if (a[n - 1] == 0) {
        cout << "YES" << endl;
        int i=n-1;
        while (i >= 0) {
            int j = i;
            int f = 0;
            int onee = 0;
            while (j >= 0 && f<= a[j]) {
                f = a[j];
                onee += a[j];
                j--;
            }
            for (int k = j + 1; k < i; k++) {
            cout << "0 ";

            }
            cout << onee << " ";
            i=j;
        }
        cout << endl;
    } else {
        cout << "NO" << endl;
    }
}
int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}   
