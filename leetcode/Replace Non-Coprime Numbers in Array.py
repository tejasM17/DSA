class Solution:
    def replaceNonCoprimes(self, nums):
        print(f"input numbers : {nums}")

        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        def lcm(a: int, b: int) -> int:
            return (a * b) // gcd(a, b)

        stack = []

        for num in nums:
            print(f"Processing num: {num}")
            stack.append(num)
            print(f"after push: {stack}")

            while len(stack) >= 2 and gcd(stack[-1], stack[-2]) > 1:
                num2 = stack.pop()
                num1 = stack.pop()
                new_num = lcm(num1, num2)
                print(
                    f"  Non-coprime: {num1}, {num2}, GCD={gcd(num1, num2)}, LCM={new_num}"
                )
                stack.append(new_num)
                print(f"  Stack after LCM: {stack}")

        print(f"Final stack: {stack}")
        return stack


sol = Solution()
print(sol.replaceNonCoprimes([6, 4, 3, 2, 7]))
