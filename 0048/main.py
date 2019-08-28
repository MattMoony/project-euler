def get_series_sum(upper):
    s = 0
    for i in range(1, upper+1):
        s+=i**i

    return s

def main():
    print("Last 10 digits: " + str(get_series_sum(1000))[-10:])

if __name__ == '__main__':
    main()