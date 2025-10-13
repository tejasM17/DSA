class Solution:
    def isSubsequence(self, s, t):
        print(f"inputs : s={s}, t={t}")
        i = 0
        for letter in t:
            if i < len(s) and s[i] == letter:
                print(f"i={i}, letter={letter}")
                i += 1
        return i == len(s)


string = "ahbgdc"
s = "axc"

soln = Solution()
print(soln.isSubsequence(s, string))
