def main():
    li = []
    x = 1
    while len(li) <= 1_000_000:
        for m in list(map(int, str(x))):
            li.append(m)
        x+=1
    print(li[0]*li[9]*li[99]*li[999]*li[9_999]*li[99_999]*li[999_999])
if __name__ == "__main__":
    main()