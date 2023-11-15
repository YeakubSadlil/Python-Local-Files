def find_kth_equality(A, B, C, k):
    # Calculate the range of possible values for a, b, and c
    min_a = 10 ** (A - 1)
    max_a = 10 ** A - 1
    min_b = 10 ** (B - 1)
    max_b = 10 ** B - 1
    min_c = 10 ** (C - 1)
    max_c = 10 ** C - 1

    # Check if the k-th equality is within the range of possible values
    if k > (max_a - min_a + 1) * (max_b - min_b + 1):
        return -1

    # Find the k-th equality
    count = 0
    for a in range(min_a, max_a + 1):
        for b in range(min_b, max_b + 1):
            c = a + b
            if min_c <= c <= max_c:
                count += 1
                if count == k:
                    return f"{a} + {b} = {c}"

    return -1


# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the parameters for the test case
    A, B, C, k = map(int, input().split())

    # Find the k-th equality
    result = find_kth_equality(A, B, C, k)

    # Print the result
    print(result)
