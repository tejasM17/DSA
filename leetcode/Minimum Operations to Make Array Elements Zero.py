class Solution:
    def minOperations(self, queries):
        def get_ops(n: int) -> int:
            res, ops, power_of_4 = 0, 0, 1
            while power_of_4 <= n:
                l = power_of_4
                r = min(n, power_of_4 * 4 - 1)
                ops += 1
                res += (r - l + 1) * ops
                power_of_4 *= 4
            return res

        total = 0
        for l, r in queries:
            total += (get_ops(r) - get_ops(l - 1) + 1) // 2
        return total
