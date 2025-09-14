class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        i = 2
        while x >= i * i:
            print(f"x : {x}")
            print(f"i*i : {i*i}")
            i += 1
        return i - 1


sol = Solution()
print(sol.mySqrt(4))
print(sol.mySqrt(12))
print(sol.mySqrt(100))
