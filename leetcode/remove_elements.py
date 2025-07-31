class Solution():
     def removElement(self, nums,val) :
          
          k = 0

          for read in range(len(nums)):
               if nums[read] != val:
                    nums[k] = nums[read]
                    k += 1
          return k

num = [1,2,3,3,2,4,3]
vl=2

sln = Solution()
k = sln.removElement(num,vl)
print(f"\nk = {k}")
print(f'the list after removal = {num[:k]}')