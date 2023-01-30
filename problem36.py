#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
def main():
    res = []
    for x in range(1, 1000001):
        if list(map(int,str(x))) == list(map(int,str(x)))[::-1] and list(map(int,str(bin(x)[2:]))) == list(map(int,str(bin(x)[2:])))[::-1]:
            res.append(x)
    print(sum(res))

if __name__ == "__main__":
    main()