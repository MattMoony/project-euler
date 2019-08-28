# Double-base palindromes ... 

def is_palindrome(n, base=10):
    n = str(n)[2:] if str(n)[:2] == '0b' else str(n)

    for a, b in [(n[i], n[-(i+1)]) for i in range(len(n))]:
        if a!=b:
            return False
    return True

def double_base_palindromes(n):
    ps = []
    for i in range(n):
        if is_palindrome(i) and is_palindrome(bin(i)):
            ps.append(i)

    return ps

def main():
    upper = 1_000_000

    print(" Sum of numbers:", sum(double_base_palindromes(upper)))
    print(" Sum of numbers:", double_base_palindromes(upper))

if __name__ == '__main__':
    main()