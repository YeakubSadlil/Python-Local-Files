tst = int(input())
for _ in range(tst):
    a, b = map(int, input().split())
    
    if (a % b == 0):
        print(2)
        print(a-1,1)
    else:
        print(1)
        print(a)
#............Yeakub.............