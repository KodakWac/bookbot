def wordCount(string):
        words = string.split()
        return len(words)

def countChars(file_contents):
    char_count = {}
    for char in file_contents:
        charLower = char.lower()
        isAlpha = charLower.isalpha()
        if isAlpha:
            if charLower in char_count:
                char_count[charLower] += 1
            else:
                char_count[charLower] = 1

    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    words_count = len(file_contents.split())

    print("--- Begin report of books/frankenstein.txt ---")

    print(f"{words_count} words found in the document")
    
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    print(countChars(file_contents))


if __name__ == '__main__':
    main()