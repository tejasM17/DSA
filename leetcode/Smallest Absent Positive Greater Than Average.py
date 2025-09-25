class Solution:
    def smallestObject(self, n):
        s = set(n)
        avg = sum(n) / len(n)

        for a in range(1, 102):
            if a not in s and a > avg:
                return a


utra = Solution()
print(utra.smallestObject([3, 4]))
