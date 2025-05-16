def main():
    book_path = "books/frankenstein.txt"  # This is the path
    text = get_book_text(book_path)       # Get the text from the path
    num_words = get_num_words(text)       # Count words in the text
    print(f"{num_words} words found in the document")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


main()
