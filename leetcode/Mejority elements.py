class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        score = 1
        for num in nums[1:]:
            if score == 0:
                candidate = num
            score += 1 if num == candidate else -1
        return candidate
