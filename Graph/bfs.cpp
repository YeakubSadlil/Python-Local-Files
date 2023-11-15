#include <bits/stdc++.h>
using namespace std;
map<int,vector<int>>adjlist;
map<int,bool>visited;
map<int,int>dstance;
map<int,int>parent;

void bfs(int startingNode)
{
    queue<int>q;
    q.push(startingNode);
    dstance[startingNode] = 0;
    visited[startingNode] = true;

    while (!q.empty())
    {
        int x = q.front();
        cout<<"x "<<x<<endl;
        q.pop();
        for (int i =0;i < adjlist[x].size();i++)
        {
            if(visited[adjlist[x][i]] == false)
            {
                dstance[adjlist[x][i]] = dstance[x]+1;
                visited[adjlist[x][i]] = true;
                q.push(adjlist[x][i]);
                parent[adjlist[x][i]] = x;
            }
        }
        cout<<endl;
    }
}

int main()
{
    int node,edge;
    cin>>node>>edge;
    
    while(edge--)
    {
        int x,y; cin>>x>>y;
        adjlist[x].push_back(y);
        adjlist[y].push_back(x);
    }
    int startingNode = 1;
    bfs(startingNode);
    cout<<"shortest path from node "<<startingNode<<" to 10 is = "<<dstance[10]<<endl;
}

/*
10 13
1 2
1 3
1 4
2 6
3 7
3 8
4 7
5 10
6 10
7 8
7 9
8 5
9 10

this sample input's graph diagram>  http://www.shafaetsplanet.com/planetcoding/wp-content/uploads/2014/02/bfs4-300x296.png
*/