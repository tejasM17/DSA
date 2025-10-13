class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        result = ""
        i = 0

        for letter in t:
            if letter in t and s[i] == letter:
                result += letter
                i += 1
                print(f"letter={letter}, t={t}, i={i}, result={result}")

        return result == s


string = "ahbgdc"
s = "abc"

soln = Solution()
print(soln.isSubsequence(s, string))
