import sys
from stats import *
def get_book_text(pathtobook):
    with open(pathtobook) as text:
        contents = text.read()
        return contents

def main():
    if len(sys.argv) == 2:
        booktext = get_book_text(sys.argv[1])  
        wordcount = wordcounter(booktext)
        char_counter = get_character_count(booktext)
        sorted_char_counter = sort_character_count(char_counter)
        print("============ BOOKBOT ============")
        print('Analyzing book found at books/frankenstein.txt...')
        print("----------- Word Count ----------")
        print(f'Found {wordcount} total words')
        print('--------- Character Count -------')
        for char_dict in sorted_char_counter:
            print(str(char_dict["char"]) +": " + str(char_dict["num"]))
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()

