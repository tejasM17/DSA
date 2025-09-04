class Solution:
    def findClosest(self, x, y, z):
        d1 = abs(x - z)
        print(d1)
        d2 = abs(y - z)
        print(d2)

        if d1 > d2:
            return 2
        elif d2 > d1:
            return 1
        else:
            return 0


x, y, z = 2, 7, 4
sol = Solution()
print(sol.findClosest(x, y, z))
