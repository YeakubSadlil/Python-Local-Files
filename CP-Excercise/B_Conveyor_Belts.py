
def moves(n, x1, y1, x2, y2):
    l2 = min(min(x2, n-x2+1),min(y2, n-y2+1))
    l1 = min(min(x1, n-x1+1),min(y1, n-y1+1))
    print(abs(l2-l1))


t = int(input())
for i in range(t):
    n, x1, y1, x2, y2 = map(int, input().split())
    moves(n, x1, y1, x2, y2)
