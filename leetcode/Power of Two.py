class Solution:
    def isPowerofTwo(self, n):

        if n <= 0:
            return False

        while n > 0:
            if n % 2 != 0:
                print(n)
                return False
            n //= 2
        return n == 1


num = 8
Sol = Solution()
Sol.isPowerofTwo(num)
