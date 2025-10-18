s = "  hello world  "

a = s.split()
rev = a[::-1]

print(a)
print(rev)

res = ""
for word in range(len(rev)):
    res += rev[word]
    res += " "


print(res)
