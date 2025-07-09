if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()



mak = sum(student_marks[query_name])/3
print("{:.2f}".format(mak))
    


#                                                           FORMAT()  method

#  The format() method in Python is used to format strings dynamically. It allows inserting variables into strings with specific formatting, such as controlling decimal places, aligning text, adding padding, and more.

# 1. Left, Right, and Center Alignment


print("Left  : {:<10}!".format("Hello"))   # Left-aligned (10 width)
print("Right : {:>10}!".format("Hello"))   # Right-aligned (10 width)
print("Center: {:^10}!".format("Hello"))   # Center-aligned (10 width)
             
# output:

# Left  : Hello     !
# Right :      Hello!
# Center:   Hello   !


#  2. Formatting Percentages

accuracy = 0.92345
print("Accuracy: {:.2%}".format(accuracy))

# output:

# Accuracy: 92.35%    
# {:.2%} → Converts to percentage with 2 decimal places.



# 3. Formatting Large Numbers with Comma Separator

number = 1000000
print("Number with commas: {:,}".format(number))

# output:

# Number with commas: 1,000,000


# 4. Formatting in Different Number Systems

num = 255
print("Binary : {:b}".format(num))   # Binary
print("Octal  : {:o}".format(num))   # Octal
print("Hex    : {:x}".format(num))   # Hexadecimal (lowercase)
print("HEX    : {:X}".format(num))   # Hexadecimal (uppercase)

# output:

# Binary : 11111111
# Octal  : 377
# Hex    : ff
# HEX    : FF


# 5. Combining Multiple Formatting Features

num = 123.4567
print("Formatted: {:>10,.2f}".format(num))

# output:
#   123.46
# {:>10,.2f} → Right-align (>10), comma-separated (,), 2 decimal places (.2f)



# 6. Formatting with Variables Inside {}
# You can pass variables inside {} using keyword arguments

print("My name is {name} and I am {age} years old.".format(name="Alice", age=25))

# Output:
# My name is Alice and I am 25 years old.

#  {name} and {age} are placeholders for named arguments.

# 7. Using format() with Dictionaries

person = {"name": "Alice", "age": 25}
print("My name is {name} and I am {age} years old.".format(**person))

# Output:
# My name is Alice and I am 25 years old.

#  **person expands dictionary keys as named placeholders.