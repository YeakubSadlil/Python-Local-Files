tsss = int(input())

for i in range(tsss):
    a, b, c = map(int, input().split())
    if a + b == c:
        print('+')
    else:
        print('-')
