# Fibonacci sequence ... 
# Not exceed 4 000 000 ... 
# Sum of even numbers ... 

def fib(n):
    if n<=1:
        return 1
    return fib(n-1) + fib(n-2)

def main():
    even_sum = 0
    i = 2

    n = fib(i)
    while n <= 4_000_000:
        even_sum += n if n%2==0 else 0
        i+=1
        n = fib(i)

    print("Even sum below 4 000 000: " + str(even_sum))

if __name__ == '__main__':
    main()