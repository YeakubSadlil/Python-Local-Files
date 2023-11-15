t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    suma = sum(a)
    minus_count = 0
    for i in range(n):
        if a[i] == -1:
            minus_count += 1
    for i in range(n-1):
        if (a[i] == -1 and a[i+1] == -1):
            minus_count = -1
    if minus_count == -1:
        print(suma+4)
    elif minus_count == 1:
        print(suma)
    elif minus_count == 0:
        print(suma-4)
    else:
        print(suma-)
    
