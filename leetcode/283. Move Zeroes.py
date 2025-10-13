class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums.sort(key=lambda x: x == 0)
