nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    cartetion = {}

    for i, num in enumerate(nums):
        if target - num in cartetion:
            return [cartetion[target - num], i]
        cartetion[num] = i
    return []


print(twoSum(nums, target))
