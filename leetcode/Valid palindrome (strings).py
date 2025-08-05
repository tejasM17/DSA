# Two ponter metod


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        for letter in s:
            if letter.isalnum():
                new_str += letter.lower()

        if new_str == new_str[::-1]:
            print(new_str)
            return True
        else:
            print("It is not Plaindrome")
            return False

    #    lef = 0
    #    rig = len(s) - 1
    #    while lef < rig:
    #        while lef < rig and not s[lef].isalnum():
    #            lef += 1
    #        while lef < rig and not s[rig].isalnum():
    #            rig -= 1
    #        if s[lef].lower() != s[rig].lower():
    #            return False
    #        lef += 1
    #        rig -= 1
    #    return True


s = "A man, a plan, a canal: Panama"
obj = Solution()
print(obj.isPalindrome(s))
print()
