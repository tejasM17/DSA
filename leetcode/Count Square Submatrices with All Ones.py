class Solution:
    def matrixSqares(self, m):
        if not m or not m[0]:
            return 0

        row = len(m)
        col = len(m[0])
        count = 0

        for i in range(row):
            for j in range(col):
                print(f"i = {i}, j = {j}")
                print(f"\nm[i][j] = {m[i][j]} count = {count}\n")
                if m[i][j] == 0:
                    continue  # dp=0, already 0, no add to count
                if i == 0 or j == 0:
                    count += m[i][j]
                else:
                    m[i][j] = min(m[i - 1][j], m[i][j - 1], m[i - 1][j - 1]) + 1
                    count += m[i][j]
        print(f"m = {row}, n = {col}")
        return count

    #    print(f"len of  m = {len(m)}")
    #    count = 0

    #    for i in range(len(m)):
    #        for j in range(len(m[i])):
    #            if m[i][j] != 1:
    #                print(m[i])
    #                print(f"len of {i} = {len(m[i])}")
    #                count = count
    #            else:
    #                count += 1
    #        print(count)


dabba = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
utram = Solution()
print(utram.matrixSqares(dabba))
