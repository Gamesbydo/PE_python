import itertools

def main():
    li = []
    for m in range(2,101):
        li.append(m)
        li.append(m)
    myset = set(itertools.permutations(li, 2))
    li.clear()
    for x in myset:
        li.append(x[0]**x[1])
    myset = set(li)
    print(len(myset))

if __name__ == "__main__":
    main()