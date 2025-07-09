# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example

# The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

# alpha
# beta
# Input Format

# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints

# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry











if __name__ == '__main__':
    l = []
    s = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name , score])
        s.add(score)
        
    low_sore = sorted(s)[1]
    low_name = []
    
    for name , score in l:
        if score == low_sore:
            low_name.append(name)
    for name in sorted(low_name):
        print(name)


# if __name__ == '__main__':
#     l = []
#     for _ in range(int(input())):
#         l.append([input(), float(input())])
    
#     sec_high = sorted(list(set([score for name,score in l])))[1]
    
#     print('\n' .join([a for a,b in sorted(l) if b == sec_high]))
        
# marksheet = []
# for _ in range(0,int(input())):
    # marksheet.append([input(), float(input())])

# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
    
