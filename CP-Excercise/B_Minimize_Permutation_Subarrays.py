# t = int(input())
# for _ in range(t):
#     n = int(input())
#     lst = list(map(int, input().split()))
#     if(lst[0] == 1 and lst[1] == 2):
#         print('2 3')
#         continue
#     print(min(lst)+1), min(lst[:min[lst]+1])

def solve():
    n = int(input())
    p = list(map(int, input().split()))

    # Find the first occurrence of a subarray that is not a permutation
    l = 0
    while l < n - 1 and p[l] < p[l + 1]:
        l += 1

    # Find the last occurrence of a subarray that is not a permutation
    r = n - 1
    while r > 0 and p[r] > p[r - 1]:
        r -= 1

    # Check if the remaining subarray is a permutation
    remaining = p[l:r + 1]
    if sorted(remaining) == remaining:
        # If the remaining subarray is a permutation, swap the first and last element
        print(l + 1, r + 1)
    else:
        # Otherwise, swap the minimum and maximum element in the subarray
        min_element = min(remaining)
        max_element = max(remaining)
        min_index = p.index(min_element)
        max_index = p.index(max_element)
        print(min_index + 1, max_index + 1)


t = int(input())
for _ in range(t):
    solve()
