class Solution:
    def canBeTypedWords(self, text, brokenLetters):
        tx = text.split(" ")
        bl = set(brokenLetters)
        count = 0

        for w in tx:
            print("word : ", w)
            if not any(c in bl for c in w):
                print(f"letter : {bl}, world : {w}")
                count += 1

        return count


utra = Solution()

print(utra.canBeTypedWords("hello world", "ad"))
print(utra.canBeTypedWords("leet code", "lt"))
print(utra.canBeTypedWords("leet code", "e"))
