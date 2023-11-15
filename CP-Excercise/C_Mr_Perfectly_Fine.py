test = int(input())

for _ in range(test):
    n = int(input())
    min_time_skill1 = float('inf')
    min_time_skill2 = float('inf')
    min_time_skill3 = float('inf')

    for _ in range(n):
        m, skills = input().split()
        m = int(m)

        if skills[0] == '1':
            min_time_skill1 = min(min_time_skill1, m)

        if skills[1] == '1':
            min_time_skill2 = min(min_time_skill2, m)

        if skills[0] == '1' and skills[1] == '1':
            min_time_skill3 = min(min_time_skill3, m)

    if min_time_skill1 == float('inf') or min_time_skill2 == float('inf'):
        print(-1)
    else:
        tmp = min_time_skill1 + min_time_skill2
        print(min(min_time_skill3,tmp))
        #.............................
