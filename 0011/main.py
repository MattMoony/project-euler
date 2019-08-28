from functools import reduce

def grid_from_file(file_name):
    s = ''
    with open(file_name, "r") as f:
        s = f.read()

    s = s.replace('\r', '').split('\n')

    for i in range(len(s)):
        s[i] = [int(x) for x in s[i].split(' ')]

    return s

def largest_product(g):
    if len(g[0])<4:
        return None

    m = reduce(lambda x,y: x*y, g[0][:4])

    for y in range(len(g)):
        for x in range(len(g[y])):
            # Horizontal
            if x-3 >= 0 and reduce(lambda a,b: a*b, g[y][x-3:x])>m:
                m = reduce(lambda a,b: a*b, g[y][x-3:x])
                print('x-', x, y)
            if x+3 < len(g[y]) and reduce(lambda x,y: x*y, g[y][x:x+3])>m:
                m = reduce(lambda a,b: a*b, g[y][x:x+4])
                print('x+', x, y)

            # Vertical
            if y-3 >= 0 and reduce(lambda a,b: a*b, [g[y-i][x] for i in range(4)])>m:
                m = reduce(lambda a,b: a*b, [g[y-i][x] for i in range(4)])
            if y+3 < len(g) and reduce(lambda a,b: a*b, [g[y+i][x] for i in range(4)])>m:
                m = reduce(lambda a,b: a*b, [g[y+i][x] for i in range(4)])

            # Diagonal
            if (x-3>=0 and y-3>=0) and reduce(lambda a,b: a*b, [g[y-i][x-i] for i in range(4)])>m:
                m = reduce(lambda a,b: a*b, [g[y-i][x-i] for i in range(4)])
            if (x+3<len(g[y]) and y+3<len(g)) and reduce(lambda a,b: a*b, [g[y+i][x+i] for i in range(4)])>m:
                m = reduce(lambda a,b: a*b, [g[y+i][x+i] for i in range(4)])
            if (x-3>=0 and y+3<len(g)) and reduce(lambda a,b: a*b, [g[y+i][x-i] for i in range(4)])>m:
                m = reduce(lambda a,b: a*b, [g[y+i][x-i] for i in range(4)])
            if (x+3<len(g[y]) and y-3>=0) and reduce(lambda a,b: a*b, [g[y-i][x+i] for i in range(4)])>m:
                m = reduce(lambda a,b: a*b, [g[y-i][x+i] for i in range(4)])

    return m

def main():
    g = grid_from_file('grid.txt')
    print(largest_product(g))

if __name__ == '__main__':
    main()