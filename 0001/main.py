def sum_ab(a, b, limit):
    s = 0

    for i in range(limit):
        if (i % a == 0) or (i % b == 0):
            s += i

    return s

def main():
    a = 3
    b = 5
    limit = 1000

    s = sum_ab(a, b, limit)
    print('Sum of multiples of [{:}, {:}]: {:} ... '.format(a, b, s))

if __name__ == '__main__':
    main()