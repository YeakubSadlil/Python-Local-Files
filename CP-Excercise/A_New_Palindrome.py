
t = int(input())
for i in range(t):
    s = input().strip()
    #find the number of distinct characters in the string
    distinct_chars = set(s)
    #find every characters frequency
    char_freq = {}
    for char in distinct_chars:
        char_freq[char] = s.count(char)
        
    if (len(distinct_chars) == 2):
        freq = {}
        c = False
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        for char, count in freq.items():
            if count == 1:
                print('NO')
                c = True
                break
        if c == False:
            print('YES')
            continue
    elif(len(distinct_chars) ==1):
        print('NO')
    else:
        print('YES')
        
    