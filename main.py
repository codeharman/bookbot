from stats import get_num_words, converter, sorting
import sys

# function goes here

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(obj):
    with open(obj) as f:
        return f.read()

def printer(items):
    result = ""
    for i in items:
        result += f"{i['char']}: {i['num']}\n"
    return result

get_num_words(get_book_text,book_path)

result = converter(get_book_text, book_path)

sorting_result = sorting(result)

printer_result = printer(sorting_result)

print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
{get_num_words(get_book_text,book_path)}
--------- Character Count -------
{printer_result}
============= END ===============
""")
