for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    present = set()
    mex = 0

    for i in a:
        present.add(i)
        while mex in present:
            mex += 1

    if mex == n:
        print("No")
    elif mex in a:
        print("Yes")
    elif 0 in a and mex == n - 1:
        print("Yes")
    else:
        print("No")
