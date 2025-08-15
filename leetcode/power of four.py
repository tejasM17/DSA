
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
    
#     class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         # Check if power of 2 and 1-bit in even position
#         return (n & (n-1)) == 0 and (n & 0xAAAAAAAA) == 0

# # Test
# n = 16
# ans = Solution()
# print(ans.isPowerOfFour(n))  # Output: True
# How It Works (Example: n = 16)

# 16 = 10000 (binary), n-1 = 15 = 01111.
# n & (n-1) = 10000 & 01111 = 00000 = 0 → Power of 2.
# 0xAAAAAAAA = 1010...1010 (1s in odd positions).
# n & 0xAAAAAAAA = 10000 & 1010...1010 = 0 → 1 bit in even position.
# True.


# Test
n = 16777216
ans = Solution()
print(ans.isPowerOfFour(n))  # Output: True

