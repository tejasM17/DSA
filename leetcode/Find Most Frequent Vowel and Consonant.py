class Solution:
    def maxFreqSum(self, s):

        count = [0] * 26
        for chr in s:
            count[ord(chr) - ord("a")] += 1
            print(f"counted {chr} : {count}")

        max_vowel = 0
        for v in "aeiou":
            freq = count[ord(v) - ord("a")]
            if freq > max_vowel:
                max_vowel = freq
            print(f"vowel '{v}' has {freq}, max_vowel = {max_vowel}")

        max_consonet = 0
        for c in "bcdfghjklmnpqrstvwxyz":
            freq = count[ord(c) - ord("a")]
            if freq > max_consonet:
                max_consonet = freq
            print(f'consonent "{c}" has {freq}, max_consonent = {max_consonet}')

        total = max_vowel + max_consonet
        return total

    #   alpha = [0] * 26
    #    for i in s:
    #        alpha[ord(i) - ord("a")] += 1
    #    vowels = set("aeiou")
    #    vows = [alpha[ord(ch) - ord("a")] for ch in vowels]
    #    cons = [alpha[i] for i in range(26) if chr(i + ord("a")) not in vowels]
    #    return max(vows) + max(cons)


s = "successes"
u = Solution()
print(u.maxFreqSum(s))
