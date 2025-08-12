# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
 
class Solution:
    def validPalindrome(self, s):
        def is_palindrome(left, right, s):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1
        
        while left < right :
            if s[left] != s[right]:
                return is_palindrome(left+1, right, s) or is_palindrome(left, right+1, s)
            left += 1
            right -= 1
        return True
        

st = "abca"
slon = Solution()
print(slon.validPalindrome(st))