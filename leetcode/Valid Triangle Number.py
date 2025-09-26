class Solution:
    def triangleNumber(self, nums) -> int:
        print(f"Input: nums={nums}")
        n = len(nums)
        if n < 3:
            print("  Less than 3 elements, returning 0")
            return 0

        nums.sort()
        print(f"  Sorted nums={nums}")

        count = 0
        for k in range(2, n):
            print(f"  Checking k={k}, nums[k]={nums[k]}")
            i, j = 0, k - 1
            while i < j:
                print(f"    i={i}, j={j}, nums[i]={nums[i]}, nums[j]={nums[j]}")
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    print(
                        f"    Valid: nums[i]+nums[j]={nums[i]+nums[j]} > nums[k], adding {j-i} triplets"
                    )
                    j -= 1
                else:
                    print(
                        f"    Invalid: nums[i]+nums[j]={nums[i]+nums[j]} <= nums[k], moving i"
                    )
                    i += 1

        print(f"  Total triplets: {count}")
        return count


t = [2, 3, 2, 4]

utra = Solution()
print(utra.triangleNumber(t))
