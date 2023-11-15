t = int(input()) # number of test cases

for _ in range(t):
    n, k = map(int, input().split())
    opinions = [input() for _ in range(n)]

    # count number of agree and disagree for each opinion
    agree = [0] * k
    disagree = [0] * k
    for i in range(n):
        for j in range(k):
            if opinions[i][j] == "+":
                agree[j] += 1
            else:
                disagree[j] += 1
    
    # calculate maximum number of members who can remain
    max_remaining = 1 # start with yourself
    for i in range(n):
        can_remain = True
        for j in range(k):
            if opinions[i][j] == "+":
                if agree[j] <= disagree[j]:
                    can_remain = False
                    break
            else:
                if disagree[j] <= agree[j]:
                    can_remain = False
                    break
        if can_remain:
            max_remaining = max(max_remaining, sum(1 for c in opinions[i] if c in "+-"))
    
    print(max_remaining)
