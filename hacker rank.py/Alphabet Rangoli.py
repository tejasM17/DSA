def print_rangoli(size):
    # your code goes here
    x=[]
    for i in range(size,0,-1):
        l=[]
        for j in range(size,i-1,-1):
            l.append(chr((j-1)+97))
        if len(l)>1:
            l=l+l[-2::-1]
        x.append(("-".join(l).center((2*(2*size-1)-1),'-')))
    x=x+x[-2::-1]
    for b in x:
        print(b)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)