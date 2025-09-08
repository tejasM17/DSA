class s:
    def getNonzeroint(self, n):
        for a in range(1, n):
            i = a
            j = n - a
            print(a)

            def iszero(z):
                return "0" not in str(z)

            if iszero(i) and iszero(j):
                print([i, j])
                return [i, j]


lis = 11
sol = s()
print(sol.getNonzeroint(lis))
