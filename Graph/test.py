"""
        0.......1
          .     .
            .   .
              . .
                2

"""

edges= [[0, 1, 5],
        [1, 2, 3],
        [0, 2, 1]]

adj = [[] for _ in range(3)]
    # Fill the adjacency list with edges and their weights
for i in range(3):
    u, v, wt = edges[i]
    adj[u].append((v, wt))
    adj[v].append((u, wt))
    
print(adj)

# import heapq

# lst = []
# heapq.heappush(lst, -1)
# heapq.heappush(lst, -3)
# heapq.heappush(lst, -0)

# print([-i for i in lst])