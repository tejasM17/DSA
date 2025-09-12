class Solution:
    def doesAliceWin(self, s: str) -> bool:
        print(f"input string : {s}")
        vowel = set("aeiou")
        for i, char in enumerate(s):
            print(f"char at {i} : {char}")
            if char in vowel:
                return True
        return False


s = Solution()
print(s.doesAliceWin("leetcoder"))
print(s.doesAliceWin("bbcd"))
print(s.doesAliceWin("leee"))
