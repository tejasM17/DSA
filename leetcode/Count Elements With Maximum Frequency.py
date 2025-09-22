class Solution:
    def maxFreqElement(self, nums):
        freq = [0] * 101
        mx = 0
        res = 0

        for n in nums:
            freq[n] += 1  # eliment count na adru index alli increase madutte
            f = freq[n]
            if f > mx:
                res = f
                mx = f
                print(f"res = {res}, mx = {mx}")
            elif f == mx:
                res += f
        return res


num = [1, 2, 2, 3, 1, 4]
s = Solution()
print(s.maxFreqElement(num))
