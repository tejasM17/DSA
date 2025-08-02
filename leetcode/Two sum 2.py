class Solution:
    def twosum(self, nums, target):
        nums.sort()
        lef, righ = 0, len(nums) - 1

        for _ in range(len(nums)):
            if lef < righ:
                sum = nums[lef] + nums[righ]
                if sum == target:
                    return [nums[lef], nums[righ]]
                    # return [left,right]
                elif sum < target:
                    lef += 1
                else:
                    righ -= 1


list1 = [
    4,
    2,
    7,
    3,
    9,
    3,
    7,
]

tosum = Solution()
print(tosum.twosum(list1, 14))


# | C/C++ Pointers       | Python Equivalent                          |
# | -------------------- | ------------------------------------------ |
# | `int *p = &x;`       | `ref = x` (for immutable) or `ref = list1` |
# | `*p = 5`             | `list[0] = 5`                              |
# | `p++` (move pointer) | Use index: `for i in range(...)`           |
# | Pass by pointer      | Function gets reference                    |

# In Python, you don’t use raw pointers but you use references (same thing, easier).

# When you pass a list or dict, it's like using a pointer.

# Learn to use indexing, slicing, and two-pointer techniques to solve problems smartly.

# Master these, and you’ll crush DSA and impress your friends on LeetCode.

# 🚀 Want to Practice?
# Try these problems on LeetCode or HackerRank using pointer-like logic:

# Two Sum II – Input Array Is Sorted

# Remove Duplicates from Sorted Array

# Move Zeroes to the End

# Reverse a List In-Place
