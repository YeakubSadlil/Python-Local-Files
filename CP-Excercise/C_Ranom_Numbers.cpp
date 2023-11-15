#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
#include <climits>
typedef long long ll;
typedef std::vector<ll> vll;
int con(char c) { switch (c) {
    case 'A':
    return 1;
    case 'B':
    return 10;
    case 'C':
    return 100;
    case 'D':
    return 1000;
    case 'E':
    return 10000;
    default:
    return 0;
}
}

ll getsum(std::string s) { ll n = s.size();
vll v(n, 0); char max_char='A';
for (ll i = n-1; i >= 0; --i) {
if (s[i] < max_char)
    v[i]=0 - con(s[i]);
    else {
    max_char = s[i];
    v[i] = con(s[i]);
}
}
ll cursum = std::accumulate(v.begin(), v.end(), 0);
return cursum;
}

