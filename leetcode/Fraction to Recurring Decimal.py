class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        print(f"Input: numerator={numerator}, denominator={denominator}")

        # numerator zero idre
        if numerator == 0:
            return "0"

        # sign
        sign = "-" if numerator * denominator < 0 else ""
        print(f"  Sign: {sign}")

        # if negetive positive ge convert madbeku
        numerator, denominator = abs(numerator), abs(denominator)

        # Integer
        integer_part = numerator // denominator
        remainder = numerator % denominator
        print(f"  Integer part: {integer_part}, Initial remainder: {remainder}")

        # if decimal illa andre
        if remainder == 0:
            print("  No decimal part, returning integer")
            return f"{sign}{integer_part}"

        # Decimal
        result = f"{sign}{integer_part}."
        remainder_map = {}  # remainder -> position in decimal part
        decimal_digits = []

        position = 0
        while remainder:
            print(f"  Position {position}: remainder={remainder}")

            # remainder repeats ?
            if remainder in remainder_map:
                # Repeating starts at remainder_map[remainder]
                start_pos = remainder_map[remainder]
                non_repeating = "".join(map(str, decimal_digits[:start_pos]))
                repeating = "".join(map(str, decimal_digits[start_pos:]))
                print(
                    f"  Repeating found at pos {start_pos}, non-repeating={non_repeating}, repeating={repeating}"
                )
                return f"{result}{non_repeating}({repeating})"

            # Store remainder , position
            remainder_map[remainder] = position

            # long division
            remainder *= 10
            digit = remainder // denominator
            decimal_digits.append(digit)
            remainder = remainder % denominator
            print(f"    Digit={digit}, New remainder={remainder}")

            position += 1

        # repeating agilla andre
        return f"{result}{''.join(map(str, decimal_digits))}"


fr1 = Solution()
print(fr1.fractionToDecimal(-4, 4))
print(fr1.fractionToDecimal(1, 2))
print(fr1.fractionToDecimal(2, 1))
print(fr1.fractionToDecimal(4, 333))
