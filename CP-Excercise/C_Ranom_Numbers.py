def calculate_value(s):
    values = {'A': 1, 'B': 10, 'C': 100, 'D': 1000, 'E': 10000}
    n = len(s)
    max_value = 0

    for i in range(n):
        current_value = values[s[i]]
        next_value = values[s[i+1]] if i+1 < n else 0

        if current_value < next_value:
            value = sum(values[ch] for ch in s[:i]) - current_value + next_value
            max_value = max(max_value, value)

    return max_value

t = int(input())
for _ in range(t):
    s = input()
    print(calculate_value(s))
