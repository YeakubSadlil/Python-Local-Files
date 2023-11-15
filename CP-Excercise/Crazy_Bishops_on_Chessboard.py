def num_moves(n):
    if n == 1:
        return 0
    elif n == 2:
        return 0
    else:
        z = ((n-3)//2)*3
        if (n-3)%2 == 1:
            return 2 + z+1
        else:
            return 2 + z

t = int(input())
for i in range(t):
    n = int(input())
    print(num_moves(n))
