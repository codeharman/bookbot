

def get_num_words(fun,inpu):
    words = fun(inpu).split()
    num_words = 0
    for i in words:
        num_words += 1
    return(f"Found {num_words} total words")

def converter(fun, inpu):
    words = fun(inpu).lower()
    num_char = {}
    for i in list(words):
        if i in num_char:
            num_char[i] += 1
        else:
            num_char[i] = 1
    return num_char

def sort_on(items):
    return items['num']

def sorting(items):
    char_list = []
    for char, val in items.items():
        if char.isalpha():
            char_list.append({
                "char": char,
                'num': val
            })
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list 

