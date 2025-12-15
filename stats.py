def count_words(text):
    return len(text.split())

def count_characters(text):
    string = text.lower()
    dictionary = {}
    for char in string:
        if char.isalpha():
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
        else:
            continue
    return dictionary

def sort_characters(chars):
    new_chars = [{"char": c, "num": n} for c, n in chars.items()]
    new_chars.sort(reverse=True, key=sort_on)
    return new_chars

def sort_on(items):
    return items["num"]