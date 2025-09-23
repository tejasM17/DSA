class Solution:
    def earliestTime(self, tasks):
        return min(sum(i) for i in tasks)


s = Solution()
print(s.earliestTime([[1, 6], [2, 3]]))
