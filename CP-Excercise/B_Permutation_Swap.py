# t = int(input())
# for _ in range(t):
#     n = int(input())
#     p = list(map(int, input().split()))
#     mx = n-1
#     lst = []
#     for i in range(0,n):
#         x = abs(i+1-p[i])
#         if x > 0:
#             lst.append(x)
#     print(min(lst))
import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m1, m2, m3 = {}, {}, {}

    for i in range(n):
        m1[a[i]] = i+1

    for i in range(n):
        m2[i+1] = i+1

    for i in range(n):
        m3[abs(m1[i+1]-m2[i+1])] = m3.get(abs(m1[i+1]-m2[i+1]), 0) + 1

    gcd = next(iter(m3))

    for x in m3:
        gcd = math.gcd(gcd, x)

    print(gcd)

