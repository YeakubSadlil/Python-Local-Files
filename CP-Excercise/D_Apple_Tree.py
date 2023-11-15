
const = int(10e5 + 10)
visited = [False] * const
store = [0] * const
ss, mm, po = 0, 0, 0
lst1 = [[] for _ in range(const)]

def dfs(x, jad=-1):
    if len(lst1[x]) == 1 and x != 1:
        store[x] = 1
    for v in lst1[x]:
        if v != jad:
            dfs(v, x)
            store[x] += store[v]

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        for i in range(1, n+1):
            lst1[i] = []
            store[i] = 0
        for i in range(1, n):
            l, r = map(int, input().split())
            lst1[l].append(r)
            lst1[r].append(l)
        dfs(1)
        m = int(input())
        lst = []
        for _ in range(m):
            l, r = map(int, input().split())
            lst.append(store[l] * store[r])
        for res in lst:
            print(res)

if __name__ == "__main__":
    main()
