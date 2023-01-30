def main():
    reslist = []
    for x in range(2,200000):
        if str(x).count("0") > 2 or str(x).count("1") > 2:
            continue
        li = []
        for y in range(len(str(x))):
            li.append(pow(int(str(x)[y]), 5))
        if x == sum(li):
            reslist.append(x)
    print(reslist)
    print(sum(reslist))
        



if __name__ == "__main__":
    main()