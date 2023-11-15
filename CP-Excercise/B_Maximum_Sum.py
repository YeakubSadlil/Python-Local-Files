

test = int(input())

for _ in range(test):
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]
    prefix_sumb = prefix_sum[:]
    
    ans = 0
    for i in range(k):
        if a[i]+a[i+1] < a[-1]:
            del a[i:i+2]
        else:
            del a[-1]
    sum1 = sum(a)

    
    ans = max(prefix_sum[-1]-prefix_sum[2*k], prefix_sum[n-k])
    ans = max(ans, sum1)
    print(ans)
    #print(prefix_sum[2*k])
    
    
    
