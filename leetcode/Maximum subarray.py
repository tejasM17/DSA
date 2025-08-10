class Solution:
    def maxSubArray(self, nums):
        current_sum = max_sum = nums[0]  # Start with the first element

        for num in nums[1:]:
            # Choose the maximum between the current number and current_sum + num
            current_sum = max(num, current_sum + num)
            # Update max_sum if current_sum is greater
            max_sum = max(max_sum, current_sum)

        return max_sum
