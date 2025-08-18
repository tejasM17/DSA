class Solution:
    def longestSubstring(self, s):
        l = 0
        m_l = 0
        letter_set = set()

        for r in range(len(s)):
            print
            while s[r] in letter_set:
                print(s[r])
                letter_set.remove(s[r])
                l += 1
            letter_set.add(s[r])
            print(f"letter settu {r} : {letter_set}")
            m_l = max(m_l, r - l + 1)
        print(f"Maximum length unique sub string : {m_l}")
        return m_l


s = "abcabcbb"
utra = Solution()
print(utra.longestSubstring(s))

# char_set = set()  # to track unique characters
# left = 0  # left side of the window
# max_length = 0

# for right in range(len(s)):
#     # If character already in window, shrink from left
#     while s[right] in char_set:
#         char_set.remove(s[left])
#         left += 1
#     print(f"s[right] : {s[right]}\n s[left] : {s[left]}")
