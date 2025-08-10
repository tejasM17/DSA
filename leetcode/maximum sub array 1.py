class Solution:
    def findMaxAvrage(self, nums, k):
        print(nums[:k])
        cur_sum = sum(nums[:k])
        print(f"cur sum : {cur_sum}")
        max_sum = cur_sum
        print(f"mx sum : {max_sum}")

        for right in range(k, len(nums)):
            print(right)
            cur_sum = cur_sum + nums[right] - nums[right - k]
            print(f"cur sum : {cur_sum}")
            max_sum = max(max_sum, cur_sum)
            print(f"max sum : {max_sum}")

        return max_sum / k


num = [1, 2, 4, 5, 2, 4, 2, 4]
k = 2
sol = Solution()

print(sol.findMaxAvrage(num, k))
