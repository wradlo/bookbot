import sys
from stats import count_characters, count_words, sort_character_counts


def get_book_text(path_to_file) -> str: # """-> str:""" at ends the function signature allows type hinting for type checkers like mypy or IDE or code editors or linters.
    # Reads the text of a book from a file and returns it as a string.
    with open(path_to_file) as f:
        file_contents = f.read() # type is str

    return file_contents

def main(path_to_book: str):
    book_text = get_book_text(path_to_book) # type is str
    # print(book_text) # Printing the book text to the console.
    num_words = count_words(book_text) # type is int
    num_characters = count_characters(book_text) # type is int
    
    print(f"Found {num_characters} total characters") # Printing the number of characters
    print(f"Found {num_words} total words") # Printing the number of words in the book.
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_count_dict = {}
    for char in book_text.lower():
        if char.isalpha():  # Check if the character is a letter
            if char in char_count_dict:
                char_count_dict[char] += 1  # Increment the count for this character in the dictionary
            else:
                char_count_dict[char] = 1  # Initialize the count for this character in the dictionary
    sorted_char_counts = sort_character_counts(char_count_dict)
    for item in sorted_char_counts:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    print(sys.argv)


if __name__ == "__main__":
    # Expect exactly one argument in addition to the script name: the path to the book file
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    main(sys.argv[1])
