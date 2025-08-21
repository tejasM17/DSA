class solution:
    def candy(self, ratings):

        n = len(ratings)
        print(len(ratings))
        if n == 0:
            return 0
        candies = [1] * n

        for a in range(1, n):
            if ratings[a] > ratings[a - 1]:
                print(ratings[a])
                print(candies)
                candies[a] = candies[a - 1] + 1
                print(f"after candy : {candies[a]}")
        for a in range(n - 2, -1, -1):
            if ratings[a] > ratings[a + 1]:
                candies[a] = max(candies[a], candies[a + 1] + 1)
        return sum(candies)


utra = solution()
print(utra.candy([1, 0, 2]))


# n = 2
# candies = [1] * 4

# print(candies)

# candies[n] = candies[n - 1] + 1

# print(candies)
# print(candies[n])
# print(candies[n - 1])
