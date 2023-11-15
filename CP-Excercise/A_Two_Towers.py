tstr = int(input())

for _ in range(tstr):
    n, m = map(int, input().split())
    s = input()
    t = input()
    cnts, cntt = 0,0
    for i in range(n-1):
        if s[i] == s[i+1]:
            cnts +=1
    for i in range(m-1):
        if t[i] == t[i+1]:
            cntt +=1
    if(cnts == 0 and cntt==0):
        print('YES')
    elif(cnts+cntt >= 2):
        print('NO')
    elif((cnts==1 and cntt == 0) or (cnts==0 and cntt == 1)):
        if(s[-1] == t[-1]):
            print('NO')
        else:
            print('YES')
    else:
        print('YES')
    