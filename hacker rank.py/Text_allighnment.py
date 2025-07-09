# In Python, a string of text can be aligned left, right and center.

# .ljust(width)

# This method returns a left aligned string of length width.

# >>> width = 20
# >>> print 'HackerRank'.ljust(width,'-')
# HackerRank----------  
# .center(width)

# This method returns a centered string of length width.

# >>> width = 20
# >>> print 'HackerRank'.center(width,'-')
# -----HackerRank-----
# .rjust(width)

# This method returns a right aligned string of length width.

# >>> width = 20
# >>> print 'HackerRank'.rjust(width,'-')
# ----------HackerRank
# Task

# You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
# Your task is to replace the blank (______) with rjust, ljust or center.

# Input Format

# A single line containing the thickness value for the logo.

# Constraints

# The thickness must be an odd number.

# Output Format

# Output the desired logo.

# Sample Input

# 5
# Sample Output

#     H    
#    HHH   
#   HHHHH  
#  HHHHHHH 
# HHHHHHHHH
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHHHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHHHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHHHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#                     HHHHHHHHH 
#                      HHHHHHH  
#                       HHHHH   
#                        HHH    
#                         H 

thickness = int (input())
c = 'H'

#Top triangle

for i in range(thickness):
    print((c * (2*i + 1)).center(2*thickness - 1))

# top pillers

for i in range(thickness + 1):
    print((c * thickness).center(2 * thickness) + (c * thickness).rjust(3 * thickness)) 

# middel line
for i in range ((thickness + 1)//2):
    print((c * (5 * thickness)).center(6 * thickness))

# bottem pillers 

for i in range (thickness):
    print  ((c * thickness).center(2 * thickness) + (c * thickness).rjust(3 * thickness))

# bottem triange 

for i in range (thickness):
    print(('H' * (2 * (thickness - 1 - i) + 1)).center(9 * thickness))











# thickness = int(input()) #This must be an odd number
# c = 'H'

# #Top Cone
# for i in range (thickness):
#     print((c * (2*i  + 1)).center(2 * thi))
# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))    

# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# # Bottom Cone
# for i in range(thickness):
#     print(('H' * (2*(thickness-1-i) + 1)).center(10*thickness - 1))