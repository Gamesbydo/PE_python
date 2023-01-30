def main():
    myset = {1,2,3}
    myset.clear()
    for x in range(1000, 10000):
        num = [1,2,3,4,5,6,7,8,9]
        for y in range(len(str(x))):
            if int(str(x)[y]) in num:
                num.pop(num.index(int(str(x)[y])))
            else:
                break
        if len(num) == 5:
            for m in range(2,int(x/2)+1):
                li = num.copy()
                if x % m == 0:
                    multi = str(m) + str(int(x/m))
                    for p in range(len(multi)):
                        if int(multi[p]) in li:
                            li.pop(li.index(int(multi[p])))
                        else:
                            break
                    if len(li) ==0:
                        print(f"The nums are: {int(x/m)} and {m} = {x}")
                        myset.add(x)
    print(myset)
    print(sum(myset))
        
if __name__ == "__main__":
    main()
#39 × 186 = 7254
#[1,3,6,8,9]