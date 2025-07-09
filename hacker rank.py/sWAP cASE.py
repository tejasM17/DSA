def swap_case(s):
    swap_letter = ""
    for letter in s:
        if letter.islower():
            swap_letter += letter.upper()
        else:
            swap_letter += letter.lower()
    return swap_letter



if __name__ == '__main__':
    s = input()                    # inpt: HackerRank.com presents "Pythonist 2".
    result = swap_case(s)
    print(result)


    #  just debug and enjoy