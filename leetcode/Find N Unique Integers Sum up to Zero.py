def sunZero(n):
    patti = []

    for a in range(1, n // 2 + 1):
        patti.append(-a)
        patti.append(a)
        print(f"a : {a}, -a : {-a}")
    print(patti)
    if n % 2 == 1:
        patti.append(0)
    return patti


print(sunZero(10))
print(sunZero(7))
