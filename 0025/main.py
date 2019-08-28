# 1000 digit fibonacci number ...

# Starting index: 1 ... 
#   F1 = 1
#   F2 = 1
#   F3 = 2
#   ...
def fib_rec(n):
    if n<=2:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

def first_fib_with_digits(digits):
    f = [1, 1]
    s = sum(f)

    while len(str(s)) < digits:
        f.pop(0)
        f.append(s)
        
        s = sum(f)

    return s

def ifirst_fib_with_digits(digits):
    f = [1, 1]
    i = 3
    s = sum(f)

    while len(str(s)) < digits:
        f.pop(0)
        f.append(s)
        
        s = sum(f)
        i+=1

    return i

def main():
    ds = 1000
    print("First %d digits fib. num was written to file 'number.txt' ... " % (ds))
    print("Index of fib. num with %d: %d" % (ds, ifirst_fib_with_digits(ds)))

    with open("number.txt", "w") as f:
        f.write(str(first_fib_with_digits(ds)))

if __name__ == '__main__':
    main()