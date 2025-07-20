class Solution:
    def LongestCommenPrefix(self, strn):

        if not strn:
            return "empt"

        if len(strn) == 1:
            return strn[0]

        ft_wr = strn[0]

        for i in range(len(ft_wr)):
            for ot_wr in strn[1:]:
                if i >= len(ot_wr) or ot_wr[i] != ft_wr[i]:
                    return ft_wr[:i]
        return ft_wr


lis1 = Solution()
n = int(input("how many strings you want to input : "))

strn = []
for a in range(n):
    strn.append(input(f"enter string {a} : "))


print(lis1.LongestCommenPrefix(strn))
