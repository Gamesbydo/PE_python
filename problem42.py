import time
def main():
    li = []
    res = 0
    _ = 0
    ##
    trig = [1]
    d=2
    while trig[-1] < 1000:
        trig.append(int(0.5*d*(d+1)))
        d+=1
    ##
    print(trig)
    file = open("p042_words.txt")
    li = (file.read()).split(",")
    for x in li:
        value = 0
        for y in x:
            if y.isalpha():    
                value += ord(y.lower()) - 96
        if value > trig[-1]:
            print("increase trig limit")
            quit()
        if value in trig:
            res +=1
        _+=1
        print(f"Words left: {len(li) - _}")
    print(f"There is: {res} triangle numbers")
            
if __name__ == "__main__":
    main()