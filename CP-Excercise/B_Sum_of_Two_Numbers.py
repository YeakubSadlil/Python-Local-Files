t = int(input().strip())
for _ in range(t):
    n1 = input()
    n = int(n1)
    if(n%20==19):
        sum_dg1,sum_dg2 = 0,0
        x,y='',''
        for i in n1:
            temp1 = (ord(i)-48)//2
            temp2 = (ord(i)-48)-temp1
            if(temp1==temp2):
                x+= str(temp1)
                y+= str(temp2)
            if(temp1>temp2): temp1,temp2=temp2,temp1
            if(sum_dg1>=sum_dg2):
                sum_dg1+=int(temp1)
                sum_dg2+=int(temp2)
                x+= str(temp1)
                y+= str(temp2)
            else:
                sum_dg1+=int(temp2)
                sum_dg2+=int(temp1)
                x+= str(temp2)
                y+= str(temp1)

        x = x.lstrip('0')
        y = y.lstrip('0')
        print(x,y)
    else:
        print(n//2,n-(n//2))