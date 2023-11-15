def solve():
    s = input()
    t = ""
    for i in range(len(s)):
        if s[i] == '_':
            if len(t) == 0 or t[-1] == '_':
                t += '^'
            t += '_'
        else:
            t += s[i]
    if len(t) == 0 or t[-1] == '_':
        t += '^'
    if len(t) == 1:
        t += '^'
    print(len(t) - len(s))

t = int(input())
for i in range(t):
    solve()
