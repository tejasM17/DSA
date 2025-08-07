class Solution:
    def minSubArraylen(self, target, nums):
        left = 0
        cur_sum = 0
        min_length = float("inf")

        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum >= target:
                min_length = min(min_length, right - left + 1)
                cur_sum -= nums[left]
                left += 1
                print(cur_sum, left, right, min_length)
        return min_length if min_length != float("inf") else 0


target = 7
nums = [2, 3, 1, 2, 4, 3]
ans = Solution()
print(ans.minSubArraylen(target, nums))
