class sol:
    def sortOvel(self, s):
        vowels = "aeiouAEIOU"
        v = sorted([ch for ch in s if ch in vowels])
        res, j = [], 0
        for ch in s:
            if ch in vowels:
                res.append(v[j])
                j += 1
            else:
                res.append(ch)
        return "".join(res)


s = sol()
print(s.sortOvel("lEetcOde"))
print(s.sortOvel("lYmpH"))
