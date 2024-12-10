import re

#FUNCTIONS
##00
def main():
    book_path = ('books/frankenstein.txt')
    file_content = get_text(book_path)

    print(f"--- Book report of {book_path} ---")
    print("")

    total_words = count_words(file_content)
    print(f"{total_words} words found in the book")
    print("")

    total_chars = chars_dict(file_content)
    sorted_by_keys = dict(sorted(total_chars.items()))
    for ele in sorted_by_keys:
        print(f"The '{ele}' character was found {sorted_by_keys[ele]} times")
    
    print("")
    print("--- End Report ---")

##01
def get_text(path):
    with open(path) as f:
        return f.read()

##02
def count_words(text):
    words = text.split()
    return len(words)

##03
def chars_dict(text):
    chars = {}
    pattern = r"[a-z]"
    for c in text:
        c = c.lower()
        x = re.match(pattern,c)
        if x:
            if c not in chars:
                chars[c] = 1
            else:
                chars[c] += 1
    
    return chars

main()
