import mblib
import itertools
def main():
    num = ["1","2","3","4","5","6","7"]
    for x in list(itertools.permutations(num, len(num)))[::-1]:
        print(f"Checking: {x}")
        if mblib.isPrime(int("".join(x))):
            res = int("".join(x))
            resdigit = len(x)
            break
    print(f"The largest is: {res} and is {resdigit}-digit")
if __name__ == "__main__":
    main()