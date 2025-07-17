def wordcounter(contents): #Takes an already open and parsed book and counts the words.
    num_words = 0
    answer = ''
    contents_list = contents.split()
    last_word = contents_list[-1] #Go to last element in list and save its value
    num_words = contents_list.index(last_word) +1 #Don't need to iterate through the list since lists have indices numerically ordered. so the last one + 1 is total.
    answer = f'{num_words} words found in the document' 
    return num_words

def get_character_count(contents): #Takes an already open and parsed book and counts the alphabetical characters:
    character_dict = {}
    for character in contents:
        if character.lower() in character_dict:
            character_dict[character.lower()] += 1
        else:
            character_dict[character.lower()] = 1
    return character_dict

def sort_character_count(character_dict):
    temp_sorter_list = []
    sorted_character_list = []
    for character in character_dict:
        if character.isalpha():
            if character not in temp_sorter_list:
                temp_sorter_list += character
    for tempcharacter in temp_sorter_list:
        char_count = {
            "char": tempcharacter,
            "num": character_dict[tempcharacter]
            }
            # Now char_count is a new dictionary in each loop

        sorted_character_list.append(char_count)
    sorted_character_list.sort(reverse=True, key=sort_on)
    return sorted_character_list

def sort_on(sorter):
    return sorter['num']


                
                
   
