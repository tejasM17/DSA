bl = set("ad")
print(bl)

tx = "leet code"
print(tx.split(" "))
tx.split(" ")

count = 0

for w in tx:
    print(w)
    for char in w:
        if char in bl:
            print(True)
            count += 1

print(count)
