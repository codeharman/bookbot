

def get_num_words(fun,inpu):
    words = fun(inpu).split()
    num_words = 0
    for i in words:
        num_words += 1
    print(f"Found {num_words} total words")


