t = int(input())
for _ in range(t):
    n = int(input())
    str = input()
    counter =1
    highest = 1
    for i in range(1,n):
        if str[i]==str[i-1]: counter+=1
        else:
            highest  = max(highest ,counter)
            counter=1
    highest  = max(highest ,counter)
    print(highest +1)
#................5555555555555555555555555555555......................