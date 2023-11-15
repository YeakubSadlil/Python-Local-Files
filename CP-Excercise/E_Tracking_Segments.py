def count_ones(a, l, r):
    return sum(a[i] == 1 for i in range(l, r+1))

def check_beautiful_segments(n, m, segments, q, changes):
    a = [0] * (n+1)
    beautiful_segments = set()

    for l, r in segments:
        ones_count = count_ones(a, l, r)
        zeros_count = (r - l + 1) - ones_count

        if ones_count > zeros_count:
            beautiful_segments.add((l, r))

    for i in range(q):
        x = changes[i]
        a[x] = 1

        for l, r in beautiful_segments.copy():
            ones_count = count_ones(a, l, r)
            zeros_count = (r - l + 1) - ones_count

            if ones_count <= zeros_count:
                beautiful_segments.remove((l, r))

        if len(beautiful_segments) > 0:
            return i + 1

    return -1

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the size of the array and the number of segments
    n, m = map(int, input().split())

    # Read the boundaries of the segments
    segments = []
    for _ in range(m):
        l, r = map(int, input().split())
        segments.append((l, r))

    # Read the number of changes
    q = int(input())

    # Read the changes
    changes = []
    for _ in range(q):
        x = int(input())
        changes.append(x)

    # Check for beautiful segments
    result = check_beautiful_segments(n, m, segments, q, changes)

    # Print the result
    print(result)
