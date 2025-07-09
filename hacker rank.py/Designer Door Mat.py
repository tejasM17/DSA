# Read Input: Get N and M.

# Top Half:

# Loop from 1 to (N-1)//2:

# For each i, calculate the number of .|. patterns: 2*i - 1.

# Create the pattern string: '.|.' * (2*i - 1).

# Center this pattern in M width, filling the sides with -.

# "WELCOME" Line:

# Center "WELCOME" in M width with -.

# Bottom Half:

# Loop from (N-1)//2 down to 1:

# Same as the top half but in reverse order.


# N, M = map(int, input().split())
# for i in range(1, (N-1)//2 + 1):
#     print(('.|.' * (2*i - 1)).center(M, '-'))
# print('WELCOME'.center(M, '-'))
# for i in range((N-1)//2, 0, -1):
#     print(('.|.' * (2*i - 1)).center(M, '-'))
N = int(input())
M = int(input())

for i in range(1 , (N - 1)//2):
    print(('.|.' * (2*i - 1)).center(M,'-'))
print('WELCOME'.center(M,'-'))
for i in range((N - 1)//2, 0, -1):
    print(('.|.' * (2*i - 1)).center(M,'-'))

