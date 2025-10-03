class Solution:
    def isPalindrome(self, x):

        print(f"input : {x}")
        utra = str(x) == str(x)[::-1] and x > 0
        return utra


x1 = 121
x2 = -121

sol = Solution()
print(sol.isPalindrome(x1))
print(sol.isPalindrome(x2))
