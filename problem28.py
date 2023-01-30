def main():
    li = []
    skip = 2
    turn = 0
    x = 1
    while x <= 1001*1001:
        li.append(x)
        x += skip
        turn +=1
        if turn == 4:
            turn = 0
            skip += 2
    print(sum(li))

if __name__ == "__main__":
    main()