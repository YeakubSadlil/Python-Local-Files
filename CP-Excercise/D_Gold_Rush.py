def recursion(n,m):
    if n == m: return True
    if m > n or n%3 != 0: return False
    return recursion(n//3,m) or recursion(n-n//3,m)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if recursion(n,m):
        print("YES")
    else:
        print("NO")




# def recursion(n,lst):
#     x = n//3
#     y= n-x
#     lst.append(x)
#     lst.append(y)
#     if(x%3==0):
#         recursion(x,lst)
#     if(y%3==0):
#         recursion(y,lst)
#     else:
#         return lst

# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     lst = []
#     if n == m:
#         print("YES")
#     elif m > n or n%3 != 0:
#         print("NO")
#     else:
#         tmp = recursion(n,lst)
#         if m in lst:
#             print("YES")
#         else:
#             print("NO")
