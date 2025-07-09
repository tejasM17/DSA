def count_substring(string, sub_string):
    count = 0
    str_len = len(string)
    sub_len = len(sub_string)
    
    if string > sub_string:
        print (count)
        
    else :
        for a in range(str_len - sub_len + 1):
            if string[a:a+sub_len] == sub_string:
                count += 1
        print(sub_len)
        return count
    
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


#     For each i in the range 0 to 4:

# Iteration 1 (i = 0):

# Slice: original[0:0+3] → "ABC".

# Compare with "CDC" → no match.

# count = 0.

# Iteration 2 (i = 1):

# Slice: original[1:1+3] → "BCD".

# Compare with "CDC" → no match.

# count = 0.

# Iteration 3 (i = 2):

# Slice: original[2:2+3] → "CDC".

# Compare with "CDC" → match.

# count = 1.

# Iteration 4 (i = 3):

# Slice: original[3:3+3] → "DCD".

# Compare with "CDC" → no match.

# count = 1.

# Iteration 5 (i = 4):

# Slice: original[4:4+3] → "CDC".

# Compare with "CDC" → match.

# count = 2.

