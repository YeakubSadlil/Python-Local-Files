t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    stack = []
    colors = [0] * n
    color = 1

    for i in range(n):
        if s[i] == '(':
            if len(stack) > 0:
                colors[i] = colors[stack[-1]]
            else:
                colors[i] = color
                color += 1
            stack.append(i)
        else:
            if len(stack) > 0:
                colors[i] = colors[stack[-1]]
                stack.pop()
            else:
                colors[i] = -1
                break

    if len(stack) > 0:
        print(-1)
    else:
        num_colors = max(colors)
        print(num_colors)
        print(" ".join(map(str, colors)))
