t = int(input())
for _ in range(t):
    n = int(input())
    lst = []
    if(n % 2==0):
        print(-1)
        continue
    else:
        while(n>1):
            if( ((n+1)//2)%2==1):
                lst.append(1)
                n = (n+1)//2
            else:
                lst.append(2)
                n = ((n+1)//2)-1
    print(len(lst))
    print(" ".join(str(x) for x in lst[::-1]))