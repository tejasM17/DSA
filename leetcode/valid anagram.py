class Soln:
    def is_anagram(self, s, t):
        
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        
str1 = "listen"
str2 = "silent"

ans = Soln()
print(ans.is_anagram(str1, str2))


# 🔹 Anagram Check in Python (Using sorted())

# Idea: Two strings are anagrams if their sorted letters match.

# sorted(): Works on any iterable → returns a new sorted list without changing the original.

# Why works: Sorting arranges letters in order; identical order → anagram.