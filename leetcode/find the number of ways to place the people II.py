class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        res = 0
        points.sort(key=lambda p: (p[0], -p[1]))

        print(points)

        for a, (x1, y1) in enumerate(points):
            y = "-inf"
            for x2, y2 in points[a + 1]:  # (x2, y2)
                if y1 >= y2 > y:
                    res += 1
                    y = y2
        return res


patti = [[1, 4], [1, 2], [2, 5], [2, 3]]
sol = Solution()

sol.numberOfPairs(patti)
