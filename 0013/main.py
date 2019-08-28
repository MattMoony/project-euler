def get_numbers(file_name):
    with open(file_name, "r") as f:
        return [int(x) for x in f.read().replace('\r', '').split('\n')]

def main():
    print("First 10 digits:", str(sum(get_numbers('./input.txt')))[:10])

if __name__ == '__main__':
    main()