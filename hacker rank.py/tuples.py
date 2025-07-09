n =  (input())  # input = 1 2 3
print(n.split()) # ['1', '2', '3']
lis = map(int, n.split()) # [1, 2, 3]
print(lis)
print(hash(tuple(lis)) ) 


#Syntax: map(function, iterable)



numbers = ['1', '2', '3']
int_numbers = map(int, numbers)  # Converts each string to an integer
print(list(int_numbers))  # Output: [1, 2, 3]


# Syntax: hash(object)

# Hashing is a process of converting input data (like a string, number, or object) into a fixed-size integer value, called a hash value or hash code.

# The hash value is used to quickly identify or compare data. For example, Python uses hashing internally for dictionaries and sets to make lookups very fast.

print(hash("tej"))  # 1551055911650831252
print(hash("tja"))  # 4657532117085273469
print(hash("teja"))  # -866158313860341946

