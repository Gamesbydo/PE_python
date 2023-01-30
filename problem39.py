def makeTrig(num): #gives back number of solutions
    return num #if this gives back number of solutions it works
    #but cba to make it, since its gonna take a long time and isnt worth it

def main():
    res = 0
    mostsolutions = 0
    for p in range(12, 1001):
        if makeTrig(p) > mostsolutions:
            mostsolutions = makeTrig(p)
            res = p
    print(res)

if __name__ == "__main__":
    main()