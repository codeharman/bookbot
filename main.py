from stats import get_num_words, converter, sorting

data = "./books/frankenstein.txt"

# function goes here

def get_book_text(obj):
    with open(obj) as f:
        return f.read()

get_num_words(get_book_text,data)
result = converter(get_book_text, data)
print(sorting(result))
print(f"""
    ============ BOOKBOT ============
    Analyzing book found at books/frankenstein.txt...
    ----------- Word Count ----------
    {get_num_words(get_book_text,data)}
    --------- Character Count -------
    ============= END ===============
""")
