def next_prime(n, primes):
    for p in primes:
        if n%p == 0:
            return next_prime(n+1, primes)
    return n

def get_prime(n):
    primes = [2]
    for i in range(n):
        primes.append(next_prime(primes[-1], primes))
    return primes[-1]

def main():
    print("Prime:", get_prime(10_001-1))

if __name__ == '__main__':
    main()