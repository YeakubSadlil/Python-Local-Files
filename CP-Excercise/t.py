inp = input()

if '+' in inp:
    inp = inp.split('+')
    a = int(inp[0]) + int(inp[1])
elif '-' in inp:
    inp = inp.split('-')
    a = int(inp[0]) - int(inp[1])
elif '*' in inp:
    inp = inp.split('*')
    a = int(inp[0]) * int(inp[1])

elif '/' in inp:
    inp = inp.split('/')
    a = int(inp[0]) / int(inp[1])

print(a)