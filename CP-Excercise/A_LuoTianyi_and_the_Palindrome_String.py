def check_all_characters_same(s):
    first_char = s[0]
    for char in s[1:]:
        if char != first_char:
            return False
    return True


test = int(input())

for _ in range(test):
    str = input()
    if(check_all_characters_same(str)): print('-1')
    else:
        print(len(str)-1)
