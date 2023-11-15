tr = int(input())
for _ in range(tr):
    num, d = map(int, input().split())
    s = input().strip()
    idx = num
    for i in range(num):
        if s[i] < str(d):
            idx = i
            break
    answer = s[:idx] + str(d) + s[idx:]
    print(answer)
