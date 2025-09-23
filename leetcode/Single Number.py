class Utra:
    def singleNum(self, nums):

        xor = 0
        print(xor)
        for num in nums:
            xor ^= num
            if num ^ xor == 0:
                print("nums are same")
            else:
                print("nums not eqal")
            print(xor)
            print(num)

        return xor


s = Utra()
print(s.singleNum([4, 1, 2, 1, 2]))
