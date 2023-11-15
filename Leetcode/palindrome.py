class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return False
        lst = []
        rem = 0
        while x != 0:
            rem = x % 10
            x = x // 10
            lst.append(rem)
        temp1 = temp2 = len(lst)+1 // 2
        temp2 -= 1
        print(temp1)
        for i in range(temp1):
            # if lst[i] != lst[temp2]:
            #     return False
            print(lst[i], lst[temp2])
            temp2 -= 1
        return lst

# Create an instance of the class
solution = Solution()

# Call the method on the instance
print(solution.isPalindrome(10))
