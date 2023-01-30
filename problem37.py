from math import sqrt
def isPrime(num):
    if num == 1:
        return False
    for y in range(2, int(sqrt(num))+1):
        if num % y == 0:
            return False
    return True

def main():
    res = []
    x = 10 #the start number
    while len(res) < 11:
        if isPrime(x):
            for y in range(1, len(str(x))):
                if isPrime(int("".join(list(str(x))[y:]))) and isPrime(int("".join(list(str(x))[:y]))) and y == len(str(x))-1:
                    res.append(x)
                    print(f"Current len: {len(res)}; list: {res}")
                    x+=1
                elif isPrime(int("".join(list(str(x))[y:]))) and isPrime(int("".join(list(str(x))[:y]))):
                    continue
                else:
                    x+=1
                    break
        else:
            x+=1
    print(f"The sum is {sum(res)}")

if __name__ == "__main__":
    main()