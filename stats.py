def count_words(text: str) -> int:
    # Counts the number of words in a given text string.
    words = text.split()  # Splits the text into words based on whitespace.
    num_words = len(words)  # Counts the number of words.
    return num_words

def count_characters(text: str) -> int:
    # Counts the number of characters in a given text string.
    num_characters = len(text.lower())  # Counts all characters including spaces and punctuation.
    dictionary = {} # Initialize an empty dictionary to hold character counts
    for char in text.lower(): # Iterate over each character in the text
        ## if char.isalpha():  # Check if the character is a letter
        if char in dictionary:
            dictionary[char] += 1 # Increment the count for this character in the dictionary
        else:
            dictionary[char] = 1 # Initialize the count for this character in the dictionary
    print(dictionary) # Print the dictionary of character counts
    # The dictionary contains the frequency of each character in the text.

    # Print dictionary sorted by character for clarity
    for char in sorted(dictionary.keys()):
        print(f"'{char}': {dictionary[char]}")  

    return num_characters

"""Add a new function to your stats.py file that takes the dictionary of characters and their counts and returns a sorted list of dictionaries.

    Each dictionary should have two key-value pairs: one for the character itself and one for that character's count (e.g. {"char": "b", "num": 4868}).
    Use the .sort() method:
        Use a helper function to return the "num" key of each dictionary for comparison.
        Sort the list from greatest to least by the count.
"""
def sort_character_counts(char_count_dict: dict) -> list:
    char_count_list = []
    for char, count in char_count_dict.items():
        char_count_list.append({"char": char, "num": count})

    def get_count(item):
        return item["num"]

    char_count_list.sort(key=get_count, reverse=True)
    return char_count_list