def next_prime(n, primes):
    for p in primes:
        if n%p == 0:
            return next_prime(n+1, primes)
    return n

def prime_sum(n):
    if n < 2:
        return 0

    primes = [2]

    while primes[-1] < n:
        primes.append(next_prime(primes[-1], primes))
        # print(primes[-1])
    primes.pop()

    return sum(primes)
def nprime_sum(n):
    if n < 2:
        return (0, [])

    primes = [2]

    while primes[-1] < n:
        primes.append(next_prime(primes[-1], primes))
    primes.pop()

    return (sum(primes), primes)

def main():
    # print("Primes:", nprime_sum(10)[1])
    print("Sum of primes:", prime_sum(2_000_000))

if __name__ == '__main__':
    main()