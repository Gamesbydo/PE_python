sequence = [1,2]
divisors = 0
mostdiv = 0
while divisors < 500:
    divisors = 1
    sequence[0] = sum(sequence)
    sequence[-1] += 1
    if sum(sequence) % 30030 != 0:
        continue
    for x in range(1,round(sum(sequence)/2)):
        if sum(sequence) % x == 0:
            divisors+=1
    if mostdiv < divisors:
        mostdiv = divisors
        print(str(mostdiv) + " - Value: " + str(sum(sequence)))
print("The value is: " + str(sum(sequence)))

# we only need sum(sequence) and the last number