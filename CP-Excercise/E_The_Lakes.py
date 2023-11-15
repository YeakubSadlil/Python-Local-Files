def dfs(grid, visited, i, j):
    n, m = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    stack = [(i, j)]
    visited[i][j] = True
    sum_depths = grid[i][j]

    while stack:
        x, y = stack.pop()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] > 0 and not visited[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = True
                sum_depths += grid[nx][ny]

    return sum_depths

tst = int(input())
for _ in range(tst):
    n, m = map(int, input().split())
    grid = []
    visited = []

    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
        visited.append([False] * m)

    max_volume = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and not visited[i][j]:
                sum_depths = dfs(grid, visited, i, j)
                max_volume = max(max_volume, sum_depths)
    print(max_volume)
