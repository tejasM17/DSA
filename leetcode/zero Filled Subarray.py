class Solution:
    def zerofieldSubarray(self, nums):
        count = 0
        result = 0

        for num in range(len(nums)):
            if nums[num] == 0:
                count += 1

            else:
                if count > 0:
                    result += (count * (count + 1)) // 2
                    count = 0

        if count > 0:
            result += count * (count + 1) // 2

        return result


lt = [1, 0, 2, 0, 3, 0, 0]
slon = Solution()
print(slon.zerofieldSubarray(lt))


# class Solution:
#     def zerofieldSubarray(self, nums):
#         lef = len(nums)
#         lst = []
#         count = 0

#         if not nums:
#             return 0

#         for num in range(len(nums)):
#             if nums[num] == 0:
#                 count += 1
#                 count * (count + 1) / 2
#                 lef += 1
#                 lst.append(nums[num])
#             else:
#                 count = 0

#             print(lst)
#             print(count)

#         return int(count * (count + 1) / 2)


# lt = [1, 0, 2, 0, 3, 0, 0, 4]
# slon = Solution()
# print(slon.zerofieldSubarray(lt))
