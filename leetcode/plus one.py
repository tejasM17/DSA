class Solution:

    def plusOne(self, digits: list[int]) -> list[int]:
                # iterate from the last digit backwards
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1   # add 1
                if digits[i] < 10:   # no carry needed
                                                                return digits
                                                                            digits[i] = 0   # reset to 0 if digit == 10, carry over
                                                                                    
                                                                                            # if all digits were 9, we need an extra 1 at the front
                                                                                                    return [1] + digits
