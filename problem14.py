longestchain = 0
longestchainvalue = 0

for x in range(1,1000000):
    num = x
    chain = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
            chain += 1
        else:
            num = 3*num +1
            chain+=1
    if num == 1 and chain > longestchain:
        longestchain = chain
        longestchainvalue = x
        print("Longest chain so far: " + str(longestchain) + ", Value: " + str(longestchainvalue))
print("Answer: " + str(longestchainvalue))