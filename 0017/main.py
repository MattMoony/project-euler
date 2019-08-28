words = [
    [
        ''    
    ],
    [
        ''
    ],
    [
        [
            '',
            'one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine'
        ],
        [
            'ten',
            'eleven',
            'twelve',
            'thirteen',
            'fourteen',
            'fifteen',
            'sixteen',
            'seventeen',
            'eighteen',
            'nineteen'
        ],
        [
            'twenty'
        ],
        [
            'thirty'
        ],
        [
            'forty'
        ],
        [
            'fifty'
        ],
        [
            'sixty'
        ],
        [
            'seventy'
        ],
        [
            'eighty'
        ],
        [
            'ninety'
        ]
    ]
]


def setup_words():
    global words

    for n in words[2][0][1:]:
        words[0].append(n + ' thousand')
        words[1].append(n + ' hundred')

    for t in words[2][2:]:
        for n in words[2][0][1:]:
            t.append(t[0] + '-' + n)

def number_to_text(n):
    n = '{:04d}'.format(n)

    s = ''

    s += words[0][int(n[:1])]
    s += (' ' if len(s)>0 and words[1][int(n[1:2])] != '' else '') + words[1][int(n[1:2])]
    s += ' and ' if ((words[0][int(n[:1])] != '' or words[1][int(n[1:2])] != '') and words[2][int(n[2:3])][int(n[3:4])] != '') else ''
    s += words[2][int(n[2:3])][int(n[3:4])]

    return s

def number_of_letters(start, end):
    l = 0
    for i in range(start, end+1):
        # print(number_to_text(i))
        l += len(number_to_text(i).replace(' ', '').replace('-', ''))

    return l

def main():
    start = 1
    end = 1000

    print(number_to_text(185))
    print("Amount of letters [%d;%d]: %d" % (start, end, number_of_letters(start, end)))

setup_words()

if __name__ == '__main__':
    main()
