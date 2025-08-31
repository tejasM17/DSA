class solution:
    def longSubarray(self, nums):
        l = 0
        zero_count = 0
        mx_len = 0

        for right in range(len(nums)):
            print(right)
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                print(zero_count)
                if nums[l] == 0:
                    zero_count -= 1
                l += 1

            mx_len = max(mx_len, right - l)
        print(f"max len : {mx_len}")
        return mx_len


ob = [1, 2, 0, 3, 0, 4]
so = solution()
print(so.longSubarray(ob))
