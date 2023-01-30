def countLetters(number):
    if number == 1000:
        return 11
    three = [1,2,6,10]
    four = [4,5,9]
    five = [3,7,8]
    six = [11,12]
    seven = [15,16]
    eight = [13,14,19,18]
    nine = [17]

    six10 = [2,3,8,9]
    five10= [5,4,6]
    seven10 = [7]
    x = 0
    y=0
    letters = 0
    if number > 99:    
        if number % 100 != 0:
            letters += 3
        x = int(number / 100)# přičteme počet písmenek v číslovce + 7 (hundred)
        if x in three:
            letters += 10
        elif x in four:
            letters += 11
        elif x in five:
            letters += 12
        number -= x*100 # číslo mezi 0-99
        if number < 20: #když je čílso < 20 -> neni systematický, musíme to udělat manuálně
            if number in three:
                letters += 3
            elif number in four:
                letters += 4
            elif number in five:
                letters += 5
            elif number in six:
                letters += 6
            elif number in seven:
                letters += 7
            elif number in eight:
                letters += 8
            elif number in nine:
                letters += 9
            return letters
        else:#číslo je systematické
            y = int(number / 10)#číslo na místě 10 - mezi 2-9
            number -= 10*y
            if y in five10:
                letters += 5
            elif y in six10:
                letters += 6
            elif y in seven10:
                letters += 7
            if number in three:
                letters += 3
            elif number in four:
                letters += 4
            elif number in five:
                letters += 5
            return letters
    elif number < 20:
        if number in three:
            letters += 3
        elif number in four:
            letters += 4
        elif number in five:
            letters += 5
        elif number in six:
            letters += 6
        elif number in seven:
            letters += 7
        elif number in eight:
            letters += 8
        elif number in nine:
            letters += 9
        return letters
    else:
        k = int(number / 10)#číslo na místě 10 - mezi 2-9
        number -= 10*k
        if k in five10:
            letters += 5
        elif k in six10:
            letters += 6
        elif k in seven10:
            letters += 7
        if number in three:
            letters += 3
        elif number in four:
            letters += 4
        elif number in five:
            letters += 5
        return letters
res = 0
for p in range(1, 1001):
    res += countLetters(p)

print(res)#eleven, twelve, thirteen,fourteen, fifteen, sixteen, seventeen, eighteen, nineteen,  