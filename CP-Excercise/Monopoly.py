t = int(input())

for i in range(t):
    p, q, r, s = map(int, input().split())
    
    max_profit = max(p, q, r, s)
    total_profit = p + q + r + s - max_profit
    
    if max_profit > total_profit:
        print("YES")
    else:
        print("NO")
