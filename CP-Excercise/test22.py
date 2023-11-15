def doesCircleExist(commands):
    results = []

    for command in commands:
    
        # Check if only turns - circle always exists
        if 'G' not in command:
            results.append('YES')
            continue

        x = y = 0 
        direction = 0 # 0-North, 1-East, 2-South, 3-West

        for c in command:
            if c == 'G':
                if direction == 0: 
                    y += 1
                elif direction == 1:
                    x += 1  
                elif direction == 2:
                    y -= 1
                else:  
                    x -= 1

            elif c == 'L':
                direction = (direction - 1) % 4

            else:
                direction = (direction + 1) % 4

        # If robot returns to 0,0 while direction North, circle exists 
        if x == 0 and y == 0 and direction == 0:
            results.append('YES')
        else:
            results.append('NO')

    return results


n = int(input())
commands = [input() for _ in range(n)]

# Call the function and print the result
results = doesCircleExist(commands)
for result in results:
    print(result)