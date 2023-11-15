def super_permutation(n):
    if n == 1:
        return [1]

    if n < 4:
        return [-1]

    sp = '123'
    b = [0] * (n+1)
    for i in range(3, n+1):
        for j in range(i):
            # insert i at every possible position
            candidate = sp[:j] + str(i) + sp[j:]
            # calculate b using candidate
            bb = [0] * (i+1)
            for k in range(1, i+1):
                bb[k] = (bb[k-1] + int(candidate[k-1])) % i
            if set(bb) == set(range(i)):
                sp = candidate
                b = [0] * (n+1)
                for k in range(1, i+1):
                    b[k] = (b[k-1] + int(sp[k-1])) % n
                if set(b[1:]) == set(range(n)):
                    return list(map(int, sp))

    return [-1]

t = int(input())

for _ in range(t):
    n = int(input())
    print(*super_permutation(n))
