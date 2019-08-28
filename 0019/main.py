def leap_year(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

def first_of_year(y):
    f_day = 0

    for i in range(1900, y):
        if leap_year(i):
            f_day = (f_day+2)%7
        else:
            f_day = (f_day+1)%7

    return f_day

mdays = [31, -1, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def d_o_ms(m, y, ys, d):
    if (m == 1):
        return (ys, 1 if ys == d else 0)

    pre = d_o_ms(m-1, y, ys, d)

    stom = -1
    if (m == 3):
        stom = (pre[0] + (29 if leap_year(y) else 28)) % 7
    else:
        stom = (pre[0] + mdays[m-2]) % 7
    
    # print(str(m) + "." + str(y))
    # print(pre)
    # print(stom)
    # print("---")

    return (stom, pre[1] + (1 if stom == d else 0))

def start_day_of_months(y, d, fy=1900):
    sd = first_of_year(fy)
    count = 0

    for i in range(fy, y+1):
        count += d_o_ms(12, i, sd, d)[1]
        sd = (sd + (366 if leap_year(i) else 365)) % 7

    return count

def main():
    try:
        while True:
            print(start_day_of_months(int(input("Enter end year: ")), int(input("Enter day index: ")), 
                int(input("Enter start year: "))))
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()