t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())
    arr = input().split()
    cnt = 0
    for i in arr:
        if i[::-1] in arr:
            cnt+=1
            print(i)
            continue
    print()
    #print(cnt)
    # sorted_arr = sorted(arr)
    # first_half = sorted_arr[:n-1]
    # second_half = sorted_arr[n-1:]
    # if cnt == 2*n-2:
    #     print("YES")
    # else:
    #     print("NO")
