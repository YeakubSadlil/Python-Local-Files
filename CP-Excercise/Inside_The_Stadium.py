def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    z = 0
    ball = 1
    counter = 0
    for i in arr:
        z += i
        if(z/ball)*100 == 100:
            counter +=1
        ball +=1
    print(counter)

t = int(input())
for i in range(t):
    solve()
