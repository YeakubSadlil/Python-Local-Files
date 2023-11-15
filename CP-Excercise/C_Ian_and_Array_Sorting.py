def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    counter = 1
    for i in range(n-1, 0, -2):
        if arr[i] < arr[i-1]:
            if i-1 == 0: counter = 0
            else: arr[i-2] -= (arr[i-1] - arr[i])
        elif i-2 >= 0: arr[i-2] += (arr[i] - arr[i-1])        
    print("YES" if counter else "NO")

t = int(input())
for i in range(t):
    solve()
