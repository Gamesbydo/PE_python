import math
def isPrime(num):
    for y in range(2, int(math.sqrt(num))+1):
        if num % y == 0:
            return False
    return True

def main ():
    res = 0
    for x in range(1,1000000, 2):
        li = list(str(x))
        for m in range(len(li)):
            if isPrime(int(''.join(li))) == False:
                break
            elif m == len(li)-1:
                res+=1
            else:
                li.append(li.pop(0))
    print(res)#even though we include 1 which is not prime, at the same time we dont include 2, so it balances out
                
            
    

if __name__ == "__main__":
    main()