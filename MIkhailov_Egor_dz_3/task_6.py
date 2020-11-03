def int_func(text):
    text = chr(ord(text[0]) - 32) + text[1:]
    return text


def print_int_func(text):
    text = text.split()
    for i in range(len(text)):
        text[i] = int_func(text[i])
    print(' '.join(text))


print_int_func('''no results matched your search.''')
