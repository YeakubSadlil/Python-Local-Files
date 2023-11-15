#include<bits/stdc++.h>
using namespace std;
#define M 2e5+1
    void dfs(list<int> v[], int node, int parent=1)
    {
        int flag = 1;
        for( auto r : v[node])
        {
            cout<<"r "<<r<<" ";
            if(r != parent)
            {
                flag = 0;
                dfs(v,r,node);
            }
        }
        if(flag == 1)
            cout<<"n "<<node<<endl;
    }

    int main()
    {
        list<int> t[200];
        pair<int,int> edges[200];
        int n; cin>>n;
        for(int i = 0; i < n-1; i++)
        {
            int x,y; cin>>x>>y;
            edges[i].first = x;
            edges[i].second = y;
            //or // edges[i] = make_pair(x,y);
        }

        for(int i = 0; i < n-1; i++)
        {
            t[edges[i].first].push_back(edges[i].second);
            t[edges[i].second].push_back(edges[i].first);
        }

        dfs(t,1);
    }

/* sample input 
7
1 2
1 3
1 4
3 5
3 6
4 7

*/