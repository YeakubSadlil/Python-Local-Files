MOD = 10**9 + 7

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort(reverse=True)
        b.sort(reverse=True)
        j = 0
        ans = 1
        for i in range(n):
            while j < n and a[i] <= b[j]:
                j += 1
            ans = (ans * (i-j+1)) % MOD
        print(ans)

if __name__ == "__main__":
    solve()
