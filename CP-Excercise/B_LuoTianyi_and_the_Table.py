t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    b = list(map(int, input().split()))
    b = sorted(b,reverse=True)
    sum = 0
    sum1 = 0
    if n > m:
        c = (n-1)*m*abs(b[0]-b[-1])
        d = (m-1)*abs(b[1]-b[-1])
        sum= c+d
        
        c1 = (n-1)*m*(abs(b[-1]-b[0]))
        d1 = (m-1)*(abs(b[-1]-b[1]))
        sum1= c1+d1
        print(max(sum,sum1))
    else:
        c = (n-1)*abs(b[1]-b[-1])
        d = (m-1)*n*abs(b[0]-b[-1])
        sum= c+d

        c1 = (n-1)*(abs(b[-1]-b[0]))
        d1 = (m-1)*n*(abs(b[-1]-b[1]))
        sum1= c1+d1
        print(max(sum,sum1))
        
    


