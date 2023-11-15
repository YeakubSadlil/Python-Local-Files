def max_people(t, test_cases):
    for _ in range(t):
        n, m, x = test_cases[_]
        seats = [0] * (m + 1)  # 0 represents an unoccupied seat
        occupied = 0

        for i in range(n):
            if x[i] > 0:
                if seats[x[i]] == 0:
                    seats[x[i]] = 1
                    occupied += 1
            elif x[i] == -1:
                j = 1
                while j <= m and seats[j] != 0:
                    j += 1
                if j <= m:
                    seats[j] = 1
                    occupied += 1
            elif x[i] == -2:
                j = m
                while j >= 1 and seats[j] != 0:
                    j -= 1
                if j >= 1:
                    seats[j] = 1
                    occupied += 1

        print(occupied)


# Read the number of test cases
t = int(input())

test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    test_cases.append((n, m, x))

# Call the max_people function
max_people(t, test_cases)
