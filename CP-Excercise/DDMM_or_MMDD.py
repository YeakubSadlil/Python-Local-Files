t = int(input())
for i in range(t):
    s = input()
    d, m, y = map(int, s.split('/'))
    if 1 <= d <= 12 and 1 <= m <= 12:
        print("BOTH")
    elif 1 <= d <= 12:
        print("MM/DD/YYYY")
    elif 1 <= m <= 12:
        print("DD/MM/YYYY")
    else:
        print("NA")
