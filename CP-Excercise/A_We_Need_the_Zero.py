from functools import reduce
from operator import xor

def find_x(n, a):
    
    for x in range(128):
        b_xor = []
        for i in range(n-1):
            b_xor.append(int(a[i] ^ x))
        a = reduce(lambda u, v: u ^ v, b_xor)
        
    #     if a == 0:
    #         return x
    # return -1

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(find_x(n, a))
