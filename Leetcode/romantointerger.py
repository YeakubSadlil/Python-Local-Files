class Solution:
    def romanToInt(self, s: str) -> int:
        mapped = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        lst = []
        for i in s:
            lst.append(mapped[i])

        sum = 0
        i = 0
        while i < len(s) - 1:
            if lst[i] >= lst[i + 1]:
                sum += lst[i]
            else:
                sum1 = lst[i]
                print("s",sum1)
                while (i < len(s) - 1 and lst[i] < lst[i + 1]):
                    sum1 += lst[i + 1]
                    i += 1
                print("sum1",sum1)
                print()
                sum1 -= lst[i]
                print("lst",lst[i])
                x = lst[i]
                x -= sum1
                sum += x
            i += 1
        if i == len(s) - 1:
            sum += lst[i]
        return sum

# Test the function
sol = Solution()
result = sol.romanToInt("MCMXCIV")
print(result)
