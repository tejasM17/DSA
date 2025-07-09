# <!-- You have a number num and a number t (the number of times you can change values).

# Each time you can:

# Increase num by 1 and decrease x by 1, OR
# Decrease num by 1 and increase x by 1
# Since we want the biggest x, we should increase x as much as possible.

# How do we do that?
# Every time you use an operation, x can go up by 2
# Since we can do this t times, x increases by 2 × t -->


class Solution:
    
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t
    

print(Solution().theMaximumAchievableX(3,2))             