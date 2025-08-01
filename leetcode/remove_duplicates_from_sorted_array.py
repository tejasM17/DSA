class solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        a = 0
        for i in range(1, len(nums)):
            if nums[a] != nums[i]:
                a += 1
                nums[a] = nums[i]
        print(nums)
        return a + 1


a = solution()
ls1 = [1, 1, 2]
print(a.removeDuplicates(ls1))
