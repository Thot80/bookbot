def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters_dict = get_letter_occurences(text)
    letters_list = list(letters_dict.items())
    letters_list.sort()
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for letter_tupples in letters_list:
        if letter_tupples[0].isalpha():
            print(f"The '{letter_tupples[0]}' character was found {letter_tupples[1]} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter_occurences(text):

    letter_occurences = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter in letter_occurences:
            letter_occurences[letter] += 1
        else:
            letter_occurences[letter] = 1
    return letter_occurences


main()