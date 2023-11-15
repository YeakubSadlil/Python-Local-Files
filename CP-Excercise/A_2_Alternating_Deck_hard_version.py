t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    alice_turn = False; black = True
    alice_w = 1
    bob_w = alice_b = bob_b = 0
    rem = n-1
    for i in range(2,n+1,2):
        if(rem<= 0): break
        if(i+i+1 <= rem):
            rem -= i+i+1
            w = b = 0
            if(black):
                b = i+1
                w = i
            else:
                w = i+1
                b = i
            if(alice_turn):
                alice_b += b
                alice_w += w
            else:
                bob_b += b
                bob_w += w
        else:
            w = b = 0
            if(black):
                b = (rem+1)//2
                w = rem-b
            else:
                w = (rem+1)//2
                b = rem-w
            if(alice_turn):
                alice_b += b
                alice_w += w
            else:
                bob_b += b
                bob_w += w
            rem = 0
        alice_turn^=True
        black^=True
    print(alice_w,alice_b, bob_w,bob_b)

