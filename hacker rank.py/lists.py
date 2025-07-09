# <!-- Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Example






# : Append 1 to the list, .
# : Append 2 to the list, .
# : Insert 3 at index , .
# : Print the array.
# Output:
# [1, 3, 2]
# Input Format

# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.

# Constraints

# The elements added to the list must be integers.
# Output Format

# For each command of type print, print the list on a new line.

# Sample Input 0

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1] -->

N = int(input())

lst = list()
for i in range(N):
    cmd, *vals = input().split() # reads a line of input and splits it into a list of strings.
    print(cmd, vals)

#     input().split() reads a line of input and splits it into a list of strings.

# cmd stores the first word (the command, e.g., insert, remove, print, etc.).

# *vals captures the remaining words (if any) as a list of arguments. For example:

# If the input is insert 0 5, then:

# cmd = "insert"

# vals = ["0", "5"]
    print(cmd, vals)
    if cmd == 'print':
        print(lst)
    else:
        getattr(lst, cmd)(*map(int, vals))

# If the command is not print, it uses getattr to dynamically call a method on the list lst.

# getattr(lst, cmd) gets the method of the list corresponding to the command (e.g., insert, remove, append, etc.).

# *map(int, vals) converts the arguments (vals) from strings to integers and passes them to the method.


#  practice problum

# Now, here's a similar problem for you to practice:

# Problem: Implement a simple calculator that takes in a string input from the user and performs arithmetic operations on two numbers.

# Example input: add 2 3

# Example output: 5

# Hint: Use the getattr function to dynamically call the corresponding arithmetic operation (e.g., add, subtract, multiply, divide) on the two input numbers.

# Go ahead and try to solve it!