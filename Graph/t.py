from collections import deque,defaultdict

# q = deque()

# q.appendleft(4)
# q.appendleft(5)
# q.appendleft(6)
# q.appendleft(7)

# print(q)

# q.pop()
# print(q)

adjlist = defaultdict(list)

x,y = 4,7
adjlist[x].append(y)
adjlist[y].append(x)
x,y = 1,7
adjlist[x].append(y)
adjlist[y].append(x)
print(adjlist)