import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(path, words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for sorted_char in sorted_chars:
        print(f"{sorted_char["char"]}: {sorted_char["num"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        text = get_book_text(path)
        words = count_words(text)
        chars = count_characters(text)
        sorted_chars = sort_characters(chars)
        print_report(path, words, sorted_chars)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()