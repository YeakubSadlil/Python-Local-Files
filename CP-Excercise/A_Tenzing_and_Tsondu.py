def can_reach_favorite_number(n, x, stacks):
    for stack in stacks:
        for book in stack:
            if (x | book) == x:
                return "Yes"
    return "No"

def main():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        stacks = []
        for _ in range(3):
            stack = list(map(int, input().split()))
            stacks.append(stack)
        result = can_reach_favorite_number(n, x, stacks)
        print(result)

if __name__ == "__main__":
    main()
