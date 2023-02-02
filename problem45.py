def main():
    tnum = [1,3]
    t = 3
    pnum = [1,5]
    p = 3
    hnum = [1,6]
    h = 3
    num = 0 
    while True:
        if hnum[-1] == pnum[-1] and pnum[-1] == tnum[-1] and hnum[-1] != 40755:
            print(f"Number found: {hnum[-1]}")
            break
        else:
            num = h*(2*h-1)
            hnum.append(num)
            h+=1
            while hnum[-1] > tnum[-1]:
                num = (t*(t-1))//2
                tnum.append(num)
                t+=1
            while hnum[-1] > pnum[-1]:
                num = (p*(3*p-1))//2
                pnum.append(num)
                p+=1
            

if __name__ == "__main__":
    main()