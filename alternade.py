import sys

def alternade(word, degree=2):
    alternades = []
    for first_letter in range(0, degree):
        alt = ""
        for letter in range(first_letter, len(word), degree):
            alt += word[letter]

        if alt != "":
            alternades.append(alt)

    return alternades

def print_alternades(dictionary, word_list):
    for line in lines:
        alt = alternade(line, degree)
        if len(line) > 4 and all(x in dictionary for x in alt):
            print(line.upper() + ': makes ' + ' and '.join([x.upper() for x in alt]))

if __name__ == "__main__":
    args = sys.argv[1:]

    word_file = 'words.txt'
    degree = 2

    if len(args) == 2:
        word_file = args[0]
        degree = int(args[1])

    elif len(args) == 1:
        word_file = args[0]

    dictionary = set()

    with open(word_file) as f:
        lines = [x.rstrip() for x in f.readlines()]
        dictionary.update(lines)

    print_alternades(dictionary, lines)   