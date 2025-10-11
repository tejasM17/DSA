class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


nums = [1, 2, 3, 1]
n2 = [1, 2, 3, 4]
sol = Solution()

print(sol.containsDuplicate(nums))
print(sol.containsDuplicate(n2))
