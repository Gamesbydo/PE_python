abu = [] # list of all abundant numbers
ressum = 0
for x in range(1, 28124):
    div = []
    for y in range(1, int(x/2) + 1):
        if x % y == 0:
            div.append(y)
    if sum(div)>x:
        abu.append(x)

for z in range(1, 28124):
    bob =0
    for m in range(len(abu)):    
        if z - abu[m] < 0:
            break
        elif z - abu[m] in abu:
            bob = 1
            break
    if bob != 1:
        ressum += z

print(ressum)

    
