

def solve(s):
    return ' '.join([word.capitalize() for word in s.split(' ')])



s = input()

result = solve(s)
print(result + '\n')


# give input as "hello world"









def solve(s):
    print([world.capitalize() for world in s.split()])
    return ' '.join([world.capitalize() for world in s.split()])

s = "hello world"
# print(s.split())
print(solve(s))
# print(s.capitalize()) 

# print("hello".capitalize())  # 'Hello'

ls = ['my', 'name', 'is', 'tejas']
ls = [world.capitalize() for world in ls]
print(ls)
print(' '.join(ls))  # 'my name is tejas'