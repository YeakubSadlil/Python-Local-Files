t = int(input())

for _ in range(t):
    n = int(input())
    if(n%2==0):
        for i in range(2,2*n+1,2):
            print(i,end=" ")
    else:
        for i in range(1,n):
            print(i,end=" ")
        print(n,end=" ")
    print()
