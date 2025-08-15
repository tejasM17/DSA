
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Precompute powers of 4 up to 2^31
        
        if n <= 0:
            return False
        while n > 1:
            if n % 4 != 0:
                print(n) 
                return False
            n //= 4
        return n == 1


# Test
n = 16777216
ans = Solution()
print(ans.isPowerOfFour(n))  # Output: True

