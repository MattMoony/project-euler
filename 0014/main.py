def collatz_sequence(n):
    rl = [n]

    if n == 1:
        return [1]
    elif n%2 == 0:
        rl.extend(collatz_sequence(int(n/2)))
    else:
        rl.extend(collatz_sequence(int(3*n+1)))

    return rl

def longest_sequence(top):
    biggest = (2, len(collatz_sequence(2)))
    for i in range(3, top+1):
        res = len(collatz_sequence(i))

        if res > biggest[1]:
            biggest = (i, res)

    return biggest

def main():
    print(longest_sequence(1_000_000))
    # print(collatz_sequence(13))

if __name__ == '__main__':
    main()