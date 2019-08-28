def digit_sum(n):
    return sum([int(d) for d in str(n)])

def main():
    print("Digit sum: " + str(digit_sum(2**1000)))

if __name__ == '__main__':
    main()