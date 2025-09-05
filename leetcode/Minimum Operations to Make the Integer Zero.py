class S:
    def makeIntzero(self, n1, n2):
        if n1 == 0:
            return 0 if n2 == 0 else -1

        for a in range(61):
            t = n1 - a * n2
            print(t)

            if t < 0:
                continue

            if bin(t).count("1") <= a <= t:
                print(bin(t))
                print(bin(t).count("1"))
                print(
                    f"a={a}, ones={bin(t).count('1')}, valid={bin(t).count('1') <= a <= t}"
                )
                return a

        return -1


n1 = 3
n2 = -2
sl = S()
print(sl.makeIntzero(n1, n2))
