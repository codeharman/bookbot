import sys
from stats import get_num_words, converter, sorting

if len(sys.argv) > 1:
    book_path = sys.argv[1]
else:
    book_path = "books/frankenstein.txt"

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = converter(text)
    sorted_chars = sorting(chars_dict)

    print(f"""
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
""")
    
    for item in sorted_chars:
        print(f"('{item['char']}', {item['num']})")

    print("============= END ===============")

main()
