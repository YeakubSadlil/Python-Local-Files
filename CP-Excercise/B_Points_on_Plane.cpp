#include <assert.h>
#include <math.h>
#include <memory.h>
#include <stdio.h>
 
#include <algorithm>
#include <chrono>
#include <complex>
#include <ctime>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <random>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define ARG4(_1,_2,_3,_4,...) _4
 
#define forn3(i,l,r) for (int i = int(l); i < int(r); ++i)
#define forn2(i,n) forn3 (i, 0, n)
#define forn(...) ARG4(__VA_ARGS__, forn3, forn2) (__VA_ARGS__)
 
#define ford3(i,l,r) for (int i = int(r) - 1; i >= int(l); --i)
#define ford2(i,n) ford3 (i, 0, n)
#define ford(...) ARG4(__VA_ARGS__, ford3, ford2) (__VA_ARGS__)

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(a) ((int) (a).size())
#define all(x) (x).begin(), (x).end()

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const long long inf64 = (1LL << 62) - 1;
const long double pi = acos(-1);

template<typename T> inline T abs (T x) {return x < 0 ? -x : x;}
template<typename T> inline T sqr (T x) {return x * x;}

template<typename T1, typename T2> inline bool umx (T1& a, T2 b) {if (a < b) {a = b; return 1;} return 0;}
template<typename T1, typename T2> inline bool umn (T1& a, T2 b) {if (b < a) {a = b; return 1;} return 0;}

void Solve(int ti) {
    long long cnt;
    cin >> cnt;

    long long left = max(0LL, (long long) sqrt(cnt) - 100);
    long long right = min(cnt, (long long) sqrt(cnt) + 100);
    cout<<left<<" "<<right<<"\n";
    while (left < right) {
        long long mid = (left + right) / 2;
        if (cnt <= sqr(mid +1)) {
            right = mid;
        }
        else {
            left = mid + 1;
        }
    }

    cout << left << "\n";
}

int main () {
    ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    
    // clock_t start_clock = clock();
    
    // freopen("_input.txt", "rt", stdin);
    // freopen("_output.txt", "wt", stdout);

    int tc = 1;
    cin >> tc;
    forn (ti, tc) {
        Solve(ti);
    }
    
    // double total_seconds = (double) (clock() - start_clock) / CLOCKS_PER_SEC;
    // cerr << "Working time: " << total_seconds << "s." << endl;

    return 0;
}
