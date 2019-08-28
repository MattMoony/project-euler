# Highly divisble triangular number ...
import prime_factors
from functools import reduce

def rec_sum(n):
    if n==1:
        return 1
    return n + rec_sum(n-1)

def divisors(pf, n=1):
    dvs = []

    for x in range(len(pf)):
        dvs.append(pf[0]*n)
        cu_el = pf.pop(0)

        dvs.extend(divisors(pf.copy(), cu_el*n))

    return list(set(dvs))

def get_divisors(n):
    pfs = prime_factors.prime_factors(n)
    pfs.sort()
    dvs = divisors(pfs)
    dvs.extend([1, n])

    return dvs

def triangular_number_divisble(numbers):
    i = 1
    ps = i
    dvs = get_divisors(ps)

    while len(dvs)<numbers:
        i+=1
        ps+=i

        dvs = get_divisors(ps)
        print("%04d; %4d; %8d" % (i, len(dvs), ps))

    return ps

def main():
    ns = 500
    print("First triangular number divisible by (more than || equal to) %d numbers: %d" % (
        ns, triangular_number_divisble(ns)))

if __name__ == '__main__':
    main()
