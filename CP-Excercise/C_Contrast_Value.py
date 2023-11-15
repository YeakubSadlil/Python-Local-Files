# You are given two arrays a and b each consisting of n integers. All elements of a
# are pairwise distinct.

# Find the number of ways to reorder a such that ai>bi for all 1≤i≤n, modulo 10^9+7.

# Two ways of reordering are considered different if the resulting arrays are different.

# Input
# Each test contains multiple test cases. The first line contains the number of test cases t(1≤t≤10^4).
# The description of the test cases follows.

# The first line of each test case contains a single integer n(2≤n≤2⋅10^5) — the length of the array a and b.

# The second line of each test case contains n distinct integers a1, a2, …, an (1≤ai≤10^9) — the array a.
# It is guaranteed that all elements of a are pairwise distinct.

# The second line of each test case contains n
# integers b1, b2, …, bn(1≤bi≤10^9) — the array b.

# It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

# Output
# For each test case, output the number of ways to reorder array a such that ai>bi
# for all 1≤i≤n, modulo 10^9+7.

# Example
# input
# 5
# 6
# 9 6 8 4 5 2
# 4 1 5 6 3 1
# 3
# 4 3 2
# 3 4 9
# 1
# 2
# 1
# 3
# 2 3 4
# 1 3 3
# 12
# 2 3 7 10 23 28 29 50 69 135 420 1000
# 1 1 2 3 5 8 13 21 34 55 89 144
# output
# 32
# 0
# 1
# 0
# 13824

# solve the above problem using the following approach in python

MOD = 10**9 + 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    pairs = sorted(zip(b, a))
    ans = 1
    cnt = 0
    for b, a in pairs:
        if a > b:
            ans = (ans * (cnt+1)) % MOD
            cnt = 0
        else:
            cnt += 1
    return ans

t = int(input())
for _ in range(t):
    print(solve())
