from math import ceil

def solve():
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    cap = sum(sum(row) for row in a)
    if cap < k + 1:
        print("-1")
        return
    # Sort the capacities of rooms in descending order
    rooms = sorted([(a[i][j], i, j) for i in range(n) for j in range(m)], reverse=True)
    # Binary search for the minimum distance
    lo, hi = 0, max(n-1, m-1)
    while lo < hi:
        mid = (lo + hi) // 2
        # Try to allocate rooms based on the sorted order of capacities
        assigned = set()
        for room_cap, i, j in rooms:
            if room_cap == 0:
                continue
            if (i, j) in assigned:
                continue
            if any(max(abs(i-p_i), abs(j-p_j)) <= mid for p_i, p_j in assigned):
                continue
            assigned.add((i, j))
            if len(assigned) == k+1:
                break
        # Check if all students were assigned a room
        if len(assigned) == k+1:
            hi = mid
        else:
            lo = mid + 1
    print(lo)

t = int(input())
for _ in range(t):
    solve()
