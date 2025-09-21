class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 0
        while n >= 0:
            i += 1
            print(f"i : {i}")
            n = n - i
            print(f"n : {n}")
        return i - 1


s = Solution()
print(s.arrangeCoins(8))
