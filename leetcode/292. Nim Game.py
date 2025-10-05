class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


n = Solution()
print(n.canWinNim(4))
print(n.canWinNim(3))
print(n.canWinNim(2))
print(n.canWinNim(1))
