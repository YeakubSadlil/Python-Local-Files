t = int(input())
lst = ['a', 'b', 'c', 'd',  'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
for _ in range(t):
    n = int(input())
    s = input().lower()
    check = False
    for i in lst:
        if i in s:
            print("NO")
            check = True
            break
    if(check == True):
        continue
    if s[0] != 'm':
        print("NO")
        continue
    cnt = 1
    for i in s:
        if(i == 'm'  and cnt == 1):
            cnt += 1
        elif(i == 'e' and cnt == 2):
            cnt+=1
        elif(i == 'o' and cnt == 3):
            cnt+=1
        elif(i == 'w' and cnt == 4):
            cnt+=1
    if(cnt == 5):
        print("YES")
    else:
        print("NO")