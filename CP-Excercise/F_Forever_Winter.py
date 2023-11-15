def find_snowflake_parameters(t):
    for _ in range(t):
        n, m = map(int, input().split())
        edges = set()

        for _ in range(m):
            u, v = map(int, input().split())
            edges.add((u, v))
            edges.add((v, u))

        x = float('inf')
        y = float('inf')

        for u, v in edges:
            count_x = 0
            count_y = 0

            for a, b in edges:
                if a == u or a == v or b == u or b == v:
                    if (a == u and b != v) or (a != u and b == v):
                        count_x += 1
                    else:
                        count_y += 1

            if count_x > 0 and count_y > 0:
                x = min(x, count_x)
                y = min(y, count_y)

        print(x, y)

# Read the number of test cases
t = int(input())

# Call the function to find the snowflake parameters for each test case
find_snowflake_parameters(t)
