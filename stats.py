
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

def chars_dict_to_sorted_list(get_num_words: dict[str, int]):
    new_list = []
    for i in 
    

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

