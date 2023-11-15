def calculate_max_strength(L, R):
    max_strength = 0

    for i in range(len(L)):
        digit_L = int(L[i])
        digit_R = int(R[i])
        max_strength += abs(digit_L - digit_R)

    return max_strength


t = int(input())

for _ in range(t):
    L, R = input().split()

    max_strength = calculate_max_strength(L, R)
    print(max_strength)
