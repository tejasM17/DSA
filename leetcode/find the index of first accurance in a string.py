class Solution:
  def firstOccurance(self, s1, s2):

    if s2 in s1:
      return 0
    else:
      return -1

utra = Solution()
print(utra.firstOccurance(s1="sadbutsad", s2="sad"))
