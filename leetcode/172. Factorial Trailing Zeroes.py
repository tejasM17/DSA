class Solution:
    def tralingZerose(self, n):
        print(f"input={n}")
        res = 0

        # Since there are always more factors of 2 than
        #  5 in ( n! ), the number of trailing
        # zeroes is determined by the number
        #  of factors of 5.
        while n > 0:
            n //= 5
            res += n
        return res


n = 3
n2 = 10
n3 = 14
soln = Solution()
print(soln.tralingZerose(n))
print(soln.tralingZerose(n2))
print(soln.tralingZerose(n3))
