class Solution:
    def firstUiquChar(self, s):
        letter_count = {}
        for letter in s: 
            letter_count[letter] = letter_count.get(letter , 0) + 1
        for i in range(len(s)):
            if letter_count[s[i]] == 1:
                print(s[i])
                return i
        return -1

s = "aabb"
sol = Solution()

print(sol.firstUiquChar(s))