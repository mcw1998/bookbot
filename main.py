from stats import get_text_length
from stats import get_characters, sort_char_counts
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    book_len = get_text_length(book_text)

    print(book_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {book_len} total words")
    print("--------- Character Count -------")
    char_dict = get_characters(book_text)
    sort_char_counts(char_dict)
    print("============= END ===============")
    print(sys.argv)


main()
