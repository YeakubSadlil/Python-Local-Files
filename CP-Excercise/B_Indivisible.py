def construct_permutation(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2]
    if n == 3:
        return [-1]
    # construct a random permutation
    perm = list(range(1, n+1))
    # repeatedly swap adjacent elements until no adjacent elements violate the condition
    while True:
        swapped = False
        for i in range(n-1):
            if (perm[i+1] - perm[i]) % (i+1) == 0:
                perm[i+1], perm[i+2] = perm[i+2], perm[i+1]
                swapped = True
        if not swapped:
            break
    return perm
