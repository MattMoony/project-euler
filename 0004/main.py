# Largest palindrome product ... 
# Largest of 3-digit numbers ... 
import math

def is_palindrome(n):
    n = str(n)

    for a, b in [(n[x], n[-(x+1)]) for x in range(math.floor(len(n)/2))]:
        if a != b: return False
    return True

def get_largest_palindrome_product(number_of_digits):
    biggest = 0

    for a in range(10**number_of_digits-1, 10**(number_of_digits-1)-1, -1):
        for b in range(10**number_of_digits-1, 10**(number_of_digits-1)-1, -1):
            if is_palindrome(a*b) and a*b>biggest:
                biggest = a*b

    return biggest

def main():
    print("Largest palindrome product: " + str(get_largest_palindrome_product(3)))

if __name__ == '__main__':
    main()