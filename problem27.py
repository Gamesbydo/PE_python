def isPrime(num):
    for x in range(2,int(num/2)):
        if num % x == 0:
            return False
    return True

def main():
    longest = 0
    for y in range(-999,1000):
        a = y
        for x in range(-1000, 1001):
            b = x
            n = 0
            li = []
            while isPrime(abs(n**2 +a*n+b)):
                li.append(n)
                n+=1
            if longest < len(li):
                longest = len(li)
                print(f"with a = {a} and b = {b} we get {len(li)} consecutive primes")
                print(f"Their product is: {a*b}")

if __name__ == "__main__":
    main()
