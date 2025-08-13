class Solution:
    def canConstruct(self, str1, str2): 
        char_count= {}

        for i in str2:
            # value = my_dict.get(key, default_value)
            char_count[i] = char_count.get(i, 0) + 1

        for i in str1:
            if i not in char_count or char_count[i] == 0:
                return False
            char_count[i] -= 1
        return True
str1 = "aa"
str2 = "aabbc"

sol = Solution()
print(sol.canConstruct(str1, str2))