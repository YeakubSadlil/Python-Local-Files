trrrrrrr = int(input())
for _ in range(trrrrrrr):
    n, m = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    if(x1==1 and y1==1)or(x2==n and y2==n) or (x1==n and y1==1)or(x2==1 and y2==n) or (x1==1 and y1==n)or(x2==n and y2==1):
        print(2)
    elif(x1==1 and y1!=1)or(x1!=1 and y1==1)or(x2==1 and y2!=1)or((x2!=1 and y2==1)):
        print(3)
    elif(x1==n and y1!=n)or(x1!=n and y1==n)or(x2==n and y2!=n)or((x2!=n and y2==n)):
        print(3)
    else:
        print(4)
#dfdddddddddddddddd
#sdafasdf