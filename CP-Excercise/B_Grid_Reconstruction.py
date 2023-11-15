def sss():
    n = int(input())
    temp = [[0 for j in range(n)] for i in range(2)]
    maxim = 2*n
    temp[0][0] = maxim
    temp[1][n-1] = maxim-1
    begin = 1
    end = maxim-2
    for i in range(n-1):
        if i % 2:#;asodkfj;aslkdjf
            temp[1][i] = end-1
            temp[0][i+1] = end
            end -= 2
        else:
            #;aosidfjksa
            temp[1][i] = begin
            temp[0][i+1] = begin+1
            begin += 2
    for i in range(2):
        for j in range(n):
            print(temp[i][j], end=" ")
        print()
#siopdfj;aksdjf
t = int(input())
for i in range(t):
    sss()
    #sdfjasjdfh
    #aosdfjkaksjdf
