def isPandigital(x):
    num = [1,2,3,4,5,6,7,8,9]
    for y in range(len(str(x))):
        if int(str(x)[y]) in num:
            num.pop(num.index(int(str(x)[y])))
        else:
            return False
    return True
def main():
    res = []
    for x in range(9, 10000):
        num = ""
        if isPandigital(x) == False:
            continue
        for m in range(1, 6-len(str(x))+1):
            num += str(x*m)
        if len(num) == 9:
            if isPandigital(int(num)):
                res.append(int(num))
    print(f"The biggest number possible is {max(res)}")
        
if __name__ == "__main__":
    main()