from stats import *
def get_book_text(pathtobook):
    with open(pathtobook) as text:
        contents = text.read()
        return contents

def main():
    booktext = get_book_text("books/frankenstein.txt")  
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
main()

