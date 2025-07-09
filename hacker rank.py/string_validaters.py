if __name__ == '__main__':
    s = input()
       
for char in s:
    if char.isalnum():
        p_isal = True
    if char.isalpha():
        p_ispha = True
    if char.isdigit():
        p_isgit = True
    if char.islower():
        p_islow = True
    if char.isupper():
        p_upp = True

print(p_isal)
print(p_ispha)
print(p_isgit)
print(p_islow)
print(p_upp)

#  run and debug to analyze the string properties