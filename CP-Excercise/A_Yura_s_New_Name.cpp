#include <bits/stdc++.h>
using namespace std;
void solve() 
{
    string str;
    cin >>str;
    string tmp="";
    for(auto &it : str)
    {
        if (it=='_')
        {
            if (tmp.empty() || tmp.back() == '_') tmp.push_back('^');
            tmp.push_back('_');
        }
        else tmp.push_back(it);
    }

    if(tmp.back() == '_') tmp.push_back('^');
    else if(tmp.size()==1) tmp+='^';

    cout << tmp.size() - str.size() << endl;
}

int main()
{
    int test;
    cin>> test;
    while (test--)
        solve();
}