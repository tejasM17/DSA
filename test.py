freq = [0] * 10
print(freq)


nums = [1, 2, 2, 3, 1, 4]
mx = 0
res = 0
for n in nums:
    print(f'n = {n}"')
    freq[n] += 1  # increse count at their index
    f = freq[n]
    print(f"freq = {freq}")

    if f > mx:
        mx += 1
        res += 1
        print(f"f = {f}, mx = {mx}, res = {res}")
    elif f == mx:
        res += f

print(f"res = {res}")
