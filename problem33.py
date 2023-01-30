def main():
    reslist = []
    num = []
    denom = []
    for x in range(10, 100):
        for y in range(10,100):
            num.clear()
            denom.clear()
            cache2 = 0
            cache1 = 0
            if x <y and x % 10 != 0 and y % 10 != 0:
                for m in range(2):
                    num.append(int(str(x)[m]))
                    denom.append(int(str(y)[m]))
                if num[0] in denom:
                    cache2 = denom.pop(denom.index(num[0]))
                    cache1 = num.pop(0)
                    if x / y == num[0] /denom[0] or x/y == cache1/cache2:
                        reslist.append(f"{x}/{y}")
                elif num[1] in denom:
                    cache2 = denom.pop(denom.index(num[1]))
                    cache1 = num.pop(1)
                    if x / y == num[0] /denom[0] or x/y == cache1/cache2:
                        reslist.append(f"{x}/{y}")
    print(reslist)


if __name__ == "__main__":
    main()