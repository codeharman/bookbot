data = "./books/frankenstein.txt"

# function goes here

def get_book_text(obj):
    with open(obj) as f:
        return f.read()

def main():
    print(get_book_text(data))

main()


