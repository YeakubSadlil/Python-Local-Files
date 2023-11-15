#include<bits/stdc++.h>
using namespace std;
int visited[10000] = {};
vector<int>store;
    void dfs(int r, vector<int> vct[])
    {
        visited[r] = 1;
        store.push_back(r);
        cout<<r<<" is visited"<<endl;
        for(int i = 0; i < vct[r].size(); i++)
        {
            if(visited[vct[r][i]] == 0)
                dfs(vct[r][i],vct);
        }
    }

    int main()
    {
        int node,edge;
        cin>>node>>edge;
        vector<int> vct[1000];

        for(int i = 1; i <= edge; i++)
        {
            int x,y;
            cin>>x>>y;
            vct[x].push_back(y);
            vct[y].push_back(x);
        }

        for(int i = 1; i <= node;i++)
        {
            if(visited[i] == 0)
                dfs(i,vct);
        }

        for(int i = 0; i < node;i++)
        {
            cout<<store[i]<<" ";
        }
    }