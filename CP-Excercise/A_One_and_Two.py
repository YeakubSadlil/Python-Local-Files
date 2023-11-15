trr = int(input())
for _ in range(trr):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = lst.count(2)
    ct = 0
    ct1 =0
    if(cnt == 0):
        print(1)
    elif(cnt%2 ==0):
        for i in lst:
            ct1+=1
            if(i == 2):
                ct+=1
                if(ct==cnt//2):
                    print(ct1)
                    break
    else:
        print(-1)
