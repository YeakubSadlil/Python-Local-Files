t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    cntr = 0
    for i in range(1,n+1):
        
        if i > a[i-1] or i == a[i-1]:
            print("YES")
            cntr = 1
            break
    if(cntr == 0):
        print('NO')