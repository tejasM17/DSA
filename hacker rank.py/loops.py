#    Task
# The provided code stub reads an integer, , from STDIN. For all non-negative integers , print .

# Example

# The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

# 0
# 1
# 4
# Input Format

# The first and only line contains the integer, .

# Constraints

# 1<=n<=20

# Output Format

# Print  lines, one corresponding to each .

# Sample Input 0

# 5
# Sample Output 0

# 0
# 1
# 4
# 9
# 16



n = int(input("enter positive integer : "))

for n in  range(1,n+1):
    n = n - 1
    print (f"{n ** 2} \n")







