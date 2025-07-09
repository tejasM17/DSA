# Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

# Example




# All permutations of  are:
# .

# Print an array of the elements that do not sum to .


# Input Format

# Four integers  and , each on a separate line.

# Constraints

# Print the list in lexicographic increasing order.
x = int(input())
y = int(input())
z = int(input())
n = int(input())

lis = [(a,b,c) for a in range(x+1) for b in range(y+1) for c in range(z+1) if (a + b + c) !=n ]
lis = [(a,b,c) for a in range(x+1) for b in range(y+1) for c in range(z+1)  ]
    
print(lis)

# List comprehension to generate valid coordinates
result = [[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if (a + b + c) != n]

# Printing the final list
print(result)



# from loops

n_list = []

for a in range(x+1):
    for b in range(y+1):
        for c in range(z+1):
            n_list.append((a,b,c))
            print(n_list)

print(n_list)

# or

lis = [[a,b,c] for a  in range (x+1) for b in range (y+1) for c in range (z+1) if (a+b+c) != n]
print(lis)