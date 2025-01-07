def wordCount(string):
        words = string.split()
        return len(words)


def countChars(file_contents):
    char_count = {}
    for char in file_contents:
        charLower = char.lower()
        if charLower in char_count:
            char_count[charLower] += 1
        else:
            char_count[charLower] = 1

    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_char_count

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    print(wordCount(file_contents))
    print(countChars(file_contents))


if __name__ == '__main__':
    main()