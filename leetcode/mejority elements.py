class Solution:
    def majorityelement(self, nums):
        n = len(nums)
        maxnum = 0

        for i in range(n):
            if nums[i] > nums[i - 1]:
                maxnum = nums[i]
