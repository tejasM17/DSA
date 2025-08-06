class Solution:
    def lengthOfLastWord(self, s: str):
        rig = len(s) - 1
        while rig >= 0 and s[rig] == " ":
            rig -= 1

        end = rig
        while rig >= 0 and s[rig] != " ":
            rig -= 1
        return end - rig


st = " Hello World  "

ans = Solution()
print(ans.lengthOfLastWord(st))
