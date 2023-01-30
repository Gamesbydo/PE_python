def count_repeat(number):
    _list = [10]
    while ((_list[-1]) % number)*10 not in _list:
        _list.append((_list[-1] % number)*10)

    return len(_list)-_list.index((_list[-1] % number)*10)

def main():
    repeat_lenth = 0
    relevent_i = 2
    for i in range(2, 1000):
        if count_repeat(i) >= repeat_lenth:
            repeat_lenth = count_repeat(i)
            relevent_i = i
            print(f"{i}-{repeat_lenth}")
    print(relevent_i)

if __name__ == "__main__":
    main()

#NOT MY CODE