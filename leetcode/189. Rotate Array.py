class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        a = len(nums)
        nums.reverse()
        print(nums)
        print(len(nums))
        print((nums[:k]))
        nums[:k] = reversed(nums[:k])
        print((nums[:k]))
        print(nums[k:])
        nums[k:] = reversed(nums[k:])
        print((nums[k:]))
        return nums


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
soln = Solution()
print(soln.rotate(nums, k))
