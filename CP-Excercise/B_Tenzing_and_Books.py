def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0

    for i in range(n):
        if a[i] > x:
            break
        temp = x
        kk = a[i]
        flag = True
        while temp > 0 and kk > 0:
            bit1 = temp & 1
            bit2 = kk & 1
            if bit1 == 0 and bit2 == 1:
                flag = False
                break
            temp >>= 1
            kk >>= 1
        if flag:
            ans |= a[i]
        else:
            break

    for i in range(n):
        if b[i] > x:
            break
        temp = x
        kk = b[i]
        flag = True
        while temp > 0 and kk > 0:
            bit1 = temp & 1
            bit2 = kk & 1
            if bit1 == 0 and bit2 == 1:
                flag = False
                break
            temp >>= 1
            kk >>= 1
        if flag:
            ans |= b[i]
        else:
            break

    for i in range(n):
        if c[i] > x:
            break
        temp = x
        kk = c[i]
        flag = True
        while temp > 0 and kk > 0:
            bit1 = temp & 1
            bit2 = kk & 1
            if bit1 == 0 and bit2 == 1:
                flag = False
                break
            temp >>= 1
            kk >>= 1
        if flag:
            ans |= c[i]
        else:
            break

    if ans == x:
        print("Yes")
    else:
        print("No")


t = int(input())
for _ in range(t):
    solve()
