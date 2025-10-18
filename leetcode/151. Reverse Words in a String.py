class Solution:
    def reverseWords(self, s: str) -> str:
        make_list = s.split()
        return " ".join(make_list[::-1])


s = "the sky is blue"
t = "  hello world  "
u = "a good   example"
sol = Solution()
print(sol.reverseWords(s))
print(sol.reverseWords(t))
print(sol.reverseWords(u))
