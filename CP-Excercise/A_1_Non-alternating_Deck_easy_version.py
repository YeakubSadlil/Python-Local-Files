
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    alice_turn = False
    alice = 1
    bob = 0
    rem = n-1
    for i in range(2,n+1,2):
        if(rem<= 0):
            break
        if(i+i+1 <= rem):
            rem -= i+i+1
            if(alice_turn):
                alice += i+i+1
            else:
                bob += i+i+1
        else:
            if(alice_turn):
                alice += rem
            else:
                bob += rem
            rem = 0
        alice_turn^=True
    print(alice,bob)

