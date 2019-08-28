from string import ascii_uppercase

def get_names(file_name):
    with open(file_name, "r") as f:
        return sorted(f.read().replace('"', '').replace(' ', '').split(','))

def get_name_sum(names):
    s = 0
    for n in names:
        s += (names.index(n)+1)*sum([ascii_uppercase.index(l)+1 for l in n])

    return s

def main():
    names = get_names('p022_names.txt')
    print("Total: %d" % (get_name_sum(names)))

if __name__ == '__main__':
    main()