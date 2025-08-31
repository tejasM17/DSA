class Solution:
    def max69num(self, num: int):
      
        digit = list(str(num))
      
        for n in range(len(digit)):
            if digit[n] == "6":
                digit[n] = "9"
                break
        return int("".join(digit))

n = 9669
s = Solution()
print(s.max69num(n))
