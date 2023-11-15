trr = int(input())

for i in range(trr):
    nnn = int(input())
    a = list(map(int, input().split()))
    even_bags = 0
    odd_bags = 0
    for x in a:
        if x % 2 == 0:
            even_bags = even_bags+ x
        else:
            odd_bags = odd_bags+ x
    if (even_bags > odd_bags) or (even_bags == nnn):
        print("YES")
    else:
        print("NO")
