

def get_num_words(fun,inpu):
    words = fun(inpu).split()
    num_words = 0
    for i in words:
        num_words += 1
    print(f"Found {num_words} total words")

def converter(fun, inpu):
    words = fun(inpu).lower()
    num_char = {}
    for i in list(words):
        if i in num_char:
            num_char[i] += 1
        else:
            num_char[i] = 1
    return num_char
            

