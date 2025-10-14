class Solution:
    def isHappy(self, n: int) -> bool:
        print(f"input={n}")
        nodiagide = set()

        while n != 1 and n not in nodiagide:
            nodiagide.add(n)
            print(f"set alli ideya={nodiagide}")
            n = sum(int(num) ** 2 for num in str(n))
        return True


n = 19
sol = Solution()
print(sol.isHappy(n))
