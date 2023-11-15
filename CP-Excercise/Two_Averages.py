def max_score(n, a):
    max_score = 0
    for i in range(1, n):
        left_len = i
        right_len = n - i
        if abs(left_len - right_len) <= 1:
            continue
        subarray_len = min(left_len, right_len) - 1
        l = i - subarray_len - 1
        r = i + subarray_len
        if a[l] < a[r]:
            continue
        score = subarray_len + 1
        max_score = max(max_score, score)
    return max_score

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(max_score(n, a))
