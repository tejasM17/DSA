class solution:
    def peopleAwareOfSecret(self, n, delay, forget):
        dp = [0] * n
        dp[0] = 1
        s = 0

        for i in range(delay, n):
            s += dp[i - delay]
            dp[i] = s

            if i - forget + 1 >= 0:
                s -= dp[i - forget + 1]

        return (sum(dp[-forget:])) % (10**9 + 7)


s = solution()
print(s.peopleAwareOfSecret(6, 2, 4))  # Example 1 → Output: 5
print(s.peopleAwareOfSecret(4, 1, 3))
