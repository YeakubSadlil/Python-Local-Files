# def linearSearch(lst,key):
#     find = key
#     for i in range(len(lst)):
#         if lst[i] == find:
#             return 'found'
#     return 'not found'

#time complexity O(n**2) 



def binarySearch(lst,key):
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = low + ((high - low) // 2)
        if lst[mid] == key: return 'found'
        elif key >lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return 'not found'

n,q = map(int,input().split())
ls = list(map(int,input().split()))
ls.sort()
for i in range(1,q+1):
    a = int(input())
    f = binarySearch(ls,a)
    print(f)

#time complexity O(n*log(n))