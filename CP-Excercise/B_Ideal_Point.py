for _ in range(int(input())):
    n, k = map(int, input().split())
    cnt111,cnt222=0,0
    for i in range(n):
        l, r = map(int, input().split())
        if l == k:
            cnt111+=1
        if r == k:
            cnt222 +=1
    if(cnt111>=1 and cnt222>=1):
        print("YES")
    else:
        print("NO")
