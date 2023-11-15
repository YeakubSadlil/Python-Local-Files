t = int(input())
def longest_common_substring(s1, s2):
    lcs = ""
    for i in range(len(s1)):
        for j in range(len(s2)):
            k = 0
            while i+k < len(s1) and j+k < len(s2) and s1[i+k] == s2[j+k]:
                k += 1
            if k > len(lcs):
                lcs = s1[i:i+k]
    return lcs

for _ in range(t):
    a = input()
    b = input()
    lcs = longest_common_substring(a,b)
    if( (len(a) == 1 and len(b) == 1) and a!= b):
        print("NO")
    # elif(a == b):
    #     print("YES\n"+a)
    elif(len(lcs) >= 2):
        print("YES")
        print("*"+lcs+"*")
    else:
        loc_a = a.find(lcs)
        loc_b = b.find(lcs)
        # if( (loc_a != loc_b) or (loc_a > 0 and loc_a < (len(a)-1)) or (loc_b > 0 and loc_b < (len(a)-1)) ):
        #     print("NO")
        if( (loc_a == 0 and loc_b == 0 ) or (loc_a == len(a)-1 and loc_b == len(b)-1 ) ):
            print("YES")
            if (loc_a == 0 and loc_b == 0 ):
                print(lcs+"*")
            else:
                print("*"+lcs)
        else:
            print("NO")

        
    