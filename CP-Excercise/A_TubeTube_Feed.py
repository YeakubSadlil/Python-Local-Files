tst = int(input())

for _ in range(tst):
    n, t = map(int, input().split())
    d= list(map(int, input().split()))
    e = list(map(int, input().split()))

    max_entertainment = -1
    index=0
    for i in range(n):
        if(d[i]<=t and t>0):
            if(max_entertainment < e[i]):
                max_entertainment=e[i]
                index=i+1
        t = t-1
    if(index==0): print(-1)
    else: print(index)
    #.........................................