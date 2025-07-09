
arr = map(int , input().split())
    
    
# l = sorted(arr)
# print(l)
# win_scor = max(l)
# print(win_scor)
# while win_scor in l:
#     l.remove(win_scor)
#     print(l)
# print(max(l))

print(sorted(set(arr))[-2])