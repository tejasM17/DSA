ls = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

for a in range(len(ls)):
    if sum(ls[a]) == 0:
        print(f"True : {a + 1}")
