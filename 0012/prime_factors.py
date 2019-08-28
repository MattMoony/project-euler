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