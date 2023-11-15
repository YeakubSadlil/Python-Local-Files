def sum_of_falling_cans(t):
    for _ in range(t):
        n = int(input())
        result = 0

        # Calculate the sum of cans in each row up to the row containing the hit can
        for i in range(1, n+1):
            result += (2*i - 1)**2

        print(result)

# Read the number of test cases
t = int(input())

# Call the function to calculate the sum of falling cans for each test case
sum_of_falling_cans(t)
