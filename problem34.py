from math import factorial
import cProfile
def main():
    res = 0
    maxnum = 41000
    for x in range(3,maxnum):
        facli = 0
        for n in list(map(int,str(x))):
            facli += factorial(n)
        if facli == x:
            res += x
    print(f"Below {maxnum} the sum is {res}")
if __name__ == "__main__":
    cProfile.run('main()', sort="cumtime")