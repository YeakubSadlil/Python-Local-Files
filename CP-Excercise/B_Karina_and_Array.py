t = int(input())

while t > 0:

    n = int(input())

    if n == 2:
        a = list(map(int, input().split()))
        mul = a[0] * a[1]
        print(mul)
        t -= 1
        continue

    arr = list(map(int, input().split()))

    positiveFirst = 0
    positiveSec = 0

    negFirst = 0
    negSec = 0

    zero = 0
    for i in range(n):
        val = arr[i]
        if val == 0:
            zero += 1
        if val > 0:
            if val >= positiveFirst:
                positiveSec = positiveFirst
                positiveFirst = val
            else:
                if val > positiveSec:
                    positiveSec = val
        elif val < 0:
            if val <= negFirst:
                negSec = negFirst
                negFirst = val
            elif val < negSec:
                negSec = val

    mul1 = 0
    mul2 = 0

    if positiveFirst > 0 and positiveSec > 0 and negFirst < 0 and negSec < 0:
        mul1 = positiveFirst * positiveSec  
        mul2 = negFirst * negSec
        if mul1 > mul2:
            print(mul1)
        else:
            print(mul2)
    elif positiveFirst > 0 and positiveSec > 0:
        mul1 = positiveFirst * positiveSec
        print(mul1)
    elif negFirst < 0 and negSec < 0:
        mul2 = negFirst * negSec
        print(mul2)
    else:
        print(0)

    t -= 1
