# “I have a sorted list, and I need to remove extra repeats so each number shows up no more than twice, all in-place.”
# [1,1,1,2,2,3] → [1,1,2,2,3]
# [0,0,1,1,1,1,2,3,3] → [0,0,1,1,2,3,3]
class Solution:
    def removeDuplicates(self, nums):
        write = 0

        for read in range(len(nums)):
            if write < 2 or nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1
        return write


nums1 = [
    1,
    1,
    1,
    2,
    2,
    3,
    4,
]

remove1 = Solution()
print(remove1.removeDuplicates(nums1))


# read	nums[read]	write	Condition (write<2 or nums[read]!=nums[write-2]?)	Action	nums after write
# 0	1	0	0<2 → keep	nums[0]=1, write→1	[1,1,1,2,2,3]
# 1	1	1	1<2 → keep	nums[1]=1, write→2	[1,1,1,2,2,3]
# 2	1	2	2<2 false, but nums[2]=1 == nums[0]=1 → skip	no change	[1,1,1,2,2,3]
# 3	2	2	2<2 false, 2 != nums[0]=1 → keep	nums[2]=2, write→3	[1,1,2,2,2,3]
# 4	2	3	3<2 false, 2 != nums[1]=1 → keep	nums[3]=2, write→4	[1,1,2,2,2,3]
# 5	3	4	4<2 false, 3 != nums[2]=2 → keep	nums[4]=3, write→5	[1,1,2,2,3,3]
