# The included code stub will read an integer, , from STDIN.

# Without using any string methods, try to print the following:


# Note that "" represents the consecutive values in between.

# Example

# Print the string .

# Input Format

# The first line contains an integer .

# Constraints


# Output Format

# Print the list of integers from  through  as a string, without spaces.

# Sample Input 0

# 3
# Sample Output 0

# 123


# my code
n = int(input())


i = 0
    
while i < n:
        i += 1
        i_str = str(i)
        
        print(i_str, end="")



i = 0
while i <n:
    i+=1 
    i_str= str(i)
    print( i_str,end=' ')
print(type(i_str))


# n = int(input())
# a = ""
    
# for n in range(n):
#      n += 1    
#      a += str(n)
     
# print(a)  
# print(type(a))

print(*range(1,n+1), sep=' ')