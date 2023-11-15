t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # find the leftmost and rightmost positions that differ
    left, right = None, None
    for i in range(n):
        if a[i] != b[i]:
            if left is None:
                left = i
            right = i

    if left is None:
        # the arrays are already sorted
        print("-1 -1")
        continue

    # check if the subarray is already non-descending
    if sorted(a[left:right+1]) == a[left:right+1]:
        print(left+1, right+1)
        continue

    # extend the subarray to include the largest element in it
    max_val = max(a[left:right+1])
    while left > 0 and a[left-1] > max_val:
        left -= 1
    while right < n-1 and a[right+1] > max_val:
        right += 1

    # check if the subarray is now non-descending
    if sorted(a[left:right+1]) == a[left:right+1]:
        print(left+1, right+1)
        continue

    # if not, extend the subarray in the opposite direction
    while left > 0 and a[left-1] > a[right]:
        left -= 1
    while right < n-1 and a[right+1] < a[left]:
        right += 1

    print(left+1, right+1)
