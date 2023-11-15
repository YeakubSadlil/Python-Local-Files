from collections import deque,defaultdict
def bfs(startingNode,adjlist,visited,parent):
    visited[startingNode] = True
    distance[startingNode] = 0
    q = deque()
    q.appendleft(startingNode)
    
    while q:
        x = q.pop()
        for i in adjlist[x]:
            if not visited[i]:
                q.appendleft(i)
                visited[i] = True
                parent[i] = x
                distance[i] = distance[x] + 1
    #         elif parent[x] != i:  # Cycle detection
    #             return True
    # return False
    
if __name__ == '__main__':
    node,edges = map(int,input().split())
    # creating list
    # adjlist = {i:[] for i in range(1,node+1)}   # with normal dict
    # visited = [False]*(node+1)
    # parent = [0]*(node+1)
    # distance = [0]*(node+1)
    
    # maping key by default dic to handle larger node
    adjlist = defaultdict(list) 
    visited = defaultdict(bool)
    parent = defaultdict(int)
    distance = defaultdict(int)
    
    for _ in range(edges):
        x,y = map(int,input().split())
        adjlist[x].append(y)
        adjlist[y].append(x)
        
    startingNode = 1
    bfs(startingNode,adjlist,visited,parent)
    endnode = 10
    print("Distance from 1 to",endnode,"is =",distance[endnode])

"""    Sample input
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

"""