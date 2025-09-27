class solution:
    def largTriangleArea(self, points: list[list[int]]) -> float:
        print(f"input points : {points}")
        n = len(points)

        maxA = 0
        for a in range(n - 2):
            a0, a1 = points[a]
            for b in range(a + 1, n - 1):
                b0, b1 = points[b]
                for c in range(b + 1, n):
                    c0, c1 = points[c]
                    area = (b0 - a0) * (c1 - a1) - (b1 - a1) * (c0 - a0)
                    maxA = max(maxA, abs(area))
        return 0.5 * maxA


pnt = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
S = solution()
print(S.largTriangleArea(pnt))
