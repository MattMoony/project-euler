def sum_square_difference(nums):
    s = 0
    square_s = 0

    for i in nums:
        s+=i**2
        square_s+=i
    square_s**=2

    return abs(square_s-s)

def main():
    print("Sum square difference:", sum_square_difference(range(1, 100+1)))

if __name__ == '__main__':
    main()