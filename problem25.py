from time import perf_counter
def main():
    index = 2
    li = [1,1]
    while index < 200000:
        li.append(li[-1] + li[-2])
        index += 1
    print(index)


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"Time {end-start} seconds")