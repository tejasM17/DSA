class S:
    def climb(self, n):
        if n == 1:
            return 1

        pr2, pr1 = 1, 2

        for a in range(3, n + 1):
            cur = pr1 + pr2
            pr2 = pr1
            pr1 = cur
            print(f"pr2 : {pr2}, pr1 : {pr1}")
            print(f"a : {a}, cur : {cur}")

        return pr1


stp = 5
a = S()
print(a.climb(stp))
