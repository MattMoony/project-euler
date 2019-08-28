# Smallest multiple
from functools import reduce

def next_prime(n, primes):
    for p in primes:
        if n%p == 0:
            return next_prime(n+1, primes)
    return n

def prime_factors(n):
    i = 2
    factors = []
    primes = [i]

    while n > 1:
        while n%i == 0:
            factors.append(i)
            n/=i
        
        i = next_prime(i+1, primes)
        primes.append(i)

    return factors

def get_smallest_multiple(numbers):
    p_factors = [prime_factors(x) for x in numbers]

    ns = {}
    for factors in p_factors:
        for n in factors:
            if not n in ns.keys() or ns[n]<factors.count(n):
                # print(n, factors)
                ns[n] = factors.count(n)

    smallest_multiple = 1
    for k, v in ns.items():
        smallest_multiple *= k**v

    return smallest_multiple

def main():
    print("Smallest multiple: " + str(get_smallest_multiple(range(1, 20+1))))

if __name__ == '__main__':
    main()