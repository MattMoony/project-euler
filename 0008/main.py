import re
from functools import reduce

def largest_product(number, digits):
    number = str(number)

    b_nums = number[:digits]
    b_product = reduce(lambda x, y: int(x)*int(y), number[:digits])

    for i in range(1, len(number)-digits):
        if reduce(lambda x, y: int(x)*int(y), number[i:i+digits]) > b_product:
            b_nums = number[i:i+digits]
            b_product = reduce(lambda x, y: int(x)*int(y), number[i:i+digits])

    return [int(x) for x in b_nums]

def read_num(file_name):
    with open(file_name, "r") as f:
        return int(re.sub(r'\D', '', f.read()))

def main():
    numbers = largest_product(read_num('./number.txt'), 13)
    big_product = reduce(lambda x, y: x*y, numbers)

    print("Numbers:", numbers)
    print("Largest product:", big_product)

if __name__ == '__main__':
    main()