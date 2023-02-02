from itertools import permutations
from time import perf_counter
def main():
    numbers1_9 = [0,1,2,3,4,5,6,7,8,9]
    list_of_all_permutations = list(permutations(numbers1_9, 10))
    length_of_my_list = len(list_of_all_permutations)
    number_of_times_it_ran=0
    result = []
    for n in list_of_all_permutations:
        number_of_times_it_ran+=1
        if n[0] == 0:
            continue
        elif n[3] % 2 == 0 and (n[2]+n[3]+n[4]) % 3 == 0 and n[5] % 5 ==0 and int(str(n[4])+str(n[5])+str(n[6])) % 7 == 0 and (n[5]+n[7]-n[6]) % 11 == 0 and int(str(n[6])+str(n[7])+str(n[8])) % 13 == 0 and int(str(n[7])+str(n[8])+str(n[9])) % 17 == 0:
            temp_list = []
            for digits_of_n in n:
                temp_list.append(str(digits_of_n))
            result.append(int("".join(temp_list)))
            print(f"Added {temp_list}, Remaining: {length_of_my_list-number_of_times_it_ran}")
    print(f"The code ran {number_of_times_it_ran} times and the result is {sum(result)}")

if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"The code finished in {end - start} seconds")