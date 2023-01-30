f = open("p022_names.txt")
s = (f.read()).split(",")
for x in range(len(s)):
    s[x] = (s[x].strip('"')).lower()
s.sort()
res = 0
for x in range(len(s)):
    num = 0
    for y in range(len(s[x])):
        num += (ord(s[x][y])) -96
    #print(f"The word is {s[x]} and its value is {num} and its position is {x+1}")
    res += num * (x+1)
print(res)  
