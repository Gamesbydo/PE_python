#P=n(3n−1)/2
def main():
    pentagonal = [1,5,12]
    n = 4
    x = 2
    d = 0
    leave = False
    while leave !=True:
        for m in range(len(pentagonal[d:x])):
            if (pentagonal[x] + pentagonal[m]) > pentagonal[-1]:
                while (pentagonal[x] + pentagonal[m]) > pentagonal[-1]:
                    num = (n*(3*n-1))//2
                    pentagonal.append(num)
                    n+=1
            if (pentagonal[x] + pentagonal[m]) in pentagonal:
                d+=1
                if abs(pentagonal[x] - pentagonal[m]) in pentagonal:
                    print(f"The difference is {abs(pentagonal[x] - pentagonal[m])}")
                    leave = True
                    break
        x+=1
    
if __name__ == "__main__":
    main()