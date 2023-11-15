tr = int(input()) 

for i in range(tr):
    x, y = map(int, input().split())
    if 2*y <= 15*x:
        print("YES")
    else:
        print("NO")
