def wordCount(string):
        words = string.split()
        return len(words)

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    print(wordCount(file_contents))


if __name__ == '__main__':
    main()