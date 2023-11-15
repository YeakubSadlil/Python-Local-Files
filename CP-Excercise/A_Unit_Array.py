t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    
    neg_count = array.count(-1)
    pos_count = array.count(1)
    
    if(neg_count == pos_count):
        if(neg_count %2 == 0):
            print("0")
        else:
            print("1")
    elif(neg_count < pos_count):
        if(neg_count%2 == 0):
            print("0")
        else:
            print("1")
            
    else:
        counter = 0
        while(neg_count > pos_count):
            neg_count -= 1
            pos_count += 1
            counter += 1
            
        if(neg_count %2 == 1):
            counter += 1
        print(counter)
