#                                        score of a string


class Solution:
    
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(s[i+1])-ord(s[i])) for i in range(len(s)-1))
        

s = Solution()
print(s.scoreOfString("hello"))
#   Empty String and single character:

# If the string is empty (""), the function should return 0 because there are no adjacent characters to compare.