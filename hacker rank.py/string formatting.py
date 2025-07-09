def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    
    # Loop from 1 to number
    for i in range(1, number + 1):
        # Convert to each base
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        
        # Right-justify each value to width with spaces
        print(f"{decimal.rjust(width)} {octal.rjust(width)} {hexadecimal.rjust(width)} {binary.rjust(width)}")
  

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)



# 1. str(i).rjust(width)
# str(i): Converts the integer i to its decimal string representation
# (e.g., i = 5 → "5")

# .rjust(width): Right-justifies the string in a field of size width
# (e.g., "5".rjust(3) → " 5")

# Ensures all decimal numbers align neatly in a column.

# 2. str(oct(i)[2:]).rjust(width)
# oct(i): Converts i to its octal (base-8) string representation with a 0o prefix
# (e.g., oct(5) → "0o5")

# [2:]: Slices off the 0o prefix
# (e.g., "0o5"[2:] → "5")

# .rjust(width): Right-justifies the result
# (e.g., "5".rjust(3) → " 5")

# Ensures all octal numbers align under their column.

# 3. str(hex(i)[2:].upper()).rjust(width)
# hex(i): Converts i to its hexadecimal (base-16) string with a 0x prefix
# (e.g., hex(15) → "0xf")

# [2:]: Slices off the 0x prefix
# (e.g., "0xf"[2:] → "f")

# .upper(): Converts letters to uppercase (optional, but often preferred for readability)
# (e.g., "f".upper() → "F")

# .rjust(width): Right-justifies the result
# (e.g., "F".rjust(3) → " F")

# Ensures all hexadecimal values align uniformly.

# 4. str(bin(i)[2:]).rjust(width)
# bin(i): Converts i to its binary (base-2) string with a 0b prefix
# (e.g., bin(5) → "0b101")

# [2:]: Slices off the 0b prefix
# (e.g., "0b101"[2:] → "101")

# .rjust(width): Right-justifies the result
# (e.g., "101".rjust(3) → "101")

# Ensures binary numbers align properly, even for the longest value.

# Why width = len(bin(number)) - 2?
# The binary representation is typically the longest (e.g., 5 → 101 needs 3 chars).

# bin(number) includes 0b, so we subtract 2 to get the pure digit length.

# This width ensures all columns align perfectly, even for the largest number.