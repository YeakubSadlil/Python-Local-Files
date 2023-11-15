def binarySearch(x):
  low = 0
  high = 10**18

  while(low <= high):
    mid = low + (high-low)//2
    if(mid**2 == x):
      return 'Square'
    elif ( mid**2 > x):
      high = mid -1
    else:
      low = mid + 1
  return ('not squared')

x = 10**32
print(binarySearch(x))