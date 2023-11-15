t = int(input())

for i in range(t):
    s = input().strip()
    n = len(s)
    count1 = 1
    x = n-1
    while(x>=0):
        if(s[x]=='?'):
            if(x==0): count1=count1*9
            else: count1=count1*10
        x-=1
    if(s[0]=='0'): print(0)
    else: print(count1)
    
