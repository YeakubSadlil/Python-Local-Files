#include <bits/stdc++.h> 
using namespace std; 
map<pair<int,int>,int> mp; 
int solve(vector<vector<int>> &a_list,int p,int i){ 
    int res=0; 
    for(int j=0;j<a_list[i].size();j++)
    { 
        if(a_list[i][j]==p)continue; 
        int x=0; 
        if(mp[{p,i}]>mp[{i,a_list[i][j]}]) 
        x++; 
        res=max(res,x+solve(a_list,i,a_list[i][j]));
    }
    return res;

} 
int main() {
    int t; 
    cin>>t; 
    while(t--)
    { 
        int n; 
        cin>>n; 
        vector<vector<int>> a_list(n+1); 
        mp.clear(); 
        for(int i=0;i<n-1;i++) {
            int x,y; cin>>x>>y; 
            mp[{x,y}]=i; 
            mp[{y,x}]=i; 
            a_list[x].push_back(y);
            a_list[y].push_back(x); 
    } 
    int res=INT_MIN; 
    for(int i=0;i<a_list[1].size();i++)
    { 
        res=max(res,solve(a_list,1,a_list[1][i]));
    } 
    cout<<res+1<<endl; 
    }
return 0; 
} 
