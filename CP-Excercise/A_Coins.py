tst = int(input())
#..............................
for i in range(tst):
    n, kkk = map(int, input().split())
    if n % 2 == 0:
        print("YES")
    else:
        if( (n-kkk)%2==0):
            print("YES")
        else:
            print("NO")
