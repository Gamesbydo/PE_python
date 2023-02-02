from mblib import isPrime #this is a function from my library
def main():
    num = 3
    result = 0
    while result == 0:
        square = 1
        while isPrime(num):
            num+=2
        while isPrime(num - 2*(square**2)) == False:
                square+=1
                if (num - 2*(square**2)) < 0:
                    print(f"The number is {num}")
                    result = num
                    break
        num+=2

if __name__ == "__main__":
    main()