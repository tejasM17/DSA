class Solution:
    def areaOfMaxDiagonal(self, dimentions):
        max_diag = 0
        max_area = 0

        for len, wid in dimentions:
            cur_diag = len * len + wid * wid
            cur_area = len * wid

            if cur_diag > max_diag:
                max_diag = cur_diag
                max_area = cur_area
            elif cur_diag == max_diag:
                max_area = max(max_area, cur_area)
        return max_area


dim = [[9, 3], [8, 6]]
sol = Solution()
print(sol.areaOfMaxDiagonal(dim))
