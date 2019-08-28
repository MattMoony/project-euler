def champernownes_constant(digits):
    return '0.' + ''.join([str(i) for i in range(1, digits+1)])

def get_product(positions):
    cc = champernownes_constant(1_000_000)
    p = 1

    for i in positions:
        p *= int(cc[i+1])

    return p

def main():
    print("Product:", get_product([1, 10, 100, 1_000, 10_000, 100_000, 1_000_000]))

if __name__ == '__main__':
    main()