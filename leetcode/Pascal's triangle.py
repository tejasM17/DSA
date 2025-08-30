class Solution:
    def generate(self, numRows):
        n = numRows
        result = []

        if n <= 0:
            return []

        result.append([1])

        for a in range(1, n):
            prev = result[-1]
            new_row = [1]
            for b in range(len(prev) - 1):
                print(f"len of prev - 1 :  {len(prev) - 1}")
                new_row.append(prev[b] + prev[b + 1])
                print(f"new row : {new_row}")
            new_row.append(1)
            result.append(new_row)
        print(f"result : {result}")
        return result


norow = 5

sol = Solution()
sol.generate(norow)
