class sol:
    def sortOvel(self, s):
        vowel = "aeiouAEIOU"
        print(f"input string : {s}")

        vowel_list = []
        vowel_pos = []

        for a, char in enumerate(s):
            if char in vowel:
                vowel_list.append(char)
                print(f"vowel lis : {vowel_list}")
                print(f"vowel position : {vowel_pos}")
                vowel_pos.append(a)
                print(f'vowel "{char}" find at position : {a}')

        vowel_list.sort()
        print(f"sorted vowel  : {vowel_list}")

        res = list(s)
        print(f"res : {res}")

        for pos, vowels in zip(vowel_pos, vowel_list):
            res[pos] = vowels

        final = "".join(res)
        return final


s = sol()
print(s.sortOvel("lEetcOde"))
print(s.sortOvel("lYmpH"))
