class Solution:
    def numberOfPairs(self, points):
        points.sort(key=lambda p: (p[0], -p[1]))
        count = 0
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if x1 <= x2 and y1 >= y2:
                    valid = True
                    for k in range(n):
                        if k != i and k != j:
                            x, y = points[k]
                            if x1 <= x <= x2 and y2 <= y <= y1:
                                valid = False
                                break
                    if valid:
                        count += 1

        return count


s = Solution()
print(s.numberOfPairs([[6, 2], [4, 4], [2, 6]]))  # 2
print(s.numberOfPairs([[3, 1], [1, 3], [1, 1]]))  # 2
print(s.numberOfPairs([[1, 1], [2, 2], [3, 3]]))  # 0
