from stats import get_num_words
from stats import get_num_characters
from stats import character_list
from stats import get_form
import sys



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    characters = get_num_characters(sys.argv[1])
    text = get_num_words(sys.argv[1])
    sorted = get_form(characters)
    output = character_list(sorted)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {text} total words")
    print("--------- Character Count -------")
    for item in output:
        char = item["name"]
        count = item["num"]
        if char.isalpha() is True:
           print (f"{char}: {count}")


main()
