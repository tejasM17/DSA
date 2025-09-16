stack = []

num = "1234"
print(f"before : {stack}")


for a in num:
    stack.append(a)

print(f"after : {stack}")

a = 8
b = 3

a, b = b, a % b
print(a)
lcm = (a * b) // (a, b)
print(lcm)
