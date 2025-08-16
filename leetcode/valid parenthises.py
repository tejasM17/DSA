class Solution:
    def is_valid(self, s):
        brackets = {')':'(', ']':'[', '}':'{'}
        dabba = []
        for letter in s:
            if letter in '([{':
                dabba.append(letter)
            elif letter in ')]}':
                print(f'letter : {letter}')
                print(brackets[letter])
                print(f'dabba : {dabba}')
                if not dabba or dabba.pop() !=  brackets[letter]:
                    
                    return False
        return not dabba # len(dabba) == 0

sr = '([{}])'
slon = Solution()
print(slon.is_valid(sr))

# s = 12
# print(hash(s))
