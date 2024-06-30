
# By APL as part of boot.dev

def main():
    path_to_book = "books/frankenstein.txt"
    book_contents = extract_book_text(path_to_book)
    number_of_words = word_counter_function(book_contents)
    character_frequency_dictionary = character_frequency_function(book_contents)
    formatted_charfreqlist = format_charfreqdict_for_print(character_frequency_dictionary)
    print_output(path_to_book, number_of_words, formatted_charfreqlist)

# Function to extract text from .txt file
def extract_book_text(a_path):
    with open(a_path) as book:
        return book.read()

# Function to split by soaces and count a complete text
def word_counter_function(complete_book_text):
    split_text = complete_book_text.split()
    return len(split_text)

# Function to construct a case-insensitive character frequency counter.
def character_frequency_function(complete_book_text):
    miniscule_text = complete_book_text.lower()
    character_dictionary = {}
    for each_character in miniscule_text:
        if each_character in character_dictionary:
            character_dictionary[each_character] += 1
        else:
            character_dictionary[each_character] = 1
    return character_dictionary

# Function to return the value for associated with 'num' key
def return_num_for_char(dict):
    return dict["num"]

# Reformatting the frequency dictionary in sorted order
def format_charfreqdict_for_print(charfreqdict):
    charfreqlist = []
    for char, num in charfreqdict.items():
        new_dictionary = {"char": char, "num": num}
        charfreqlist.append(new_dictionary)
    charfreqlist.sort(reverse=True, key=return_num_for_char)
    return charfreqlist

# Function to print output:

def print_output(path_to_book, number_of_words, formatted_charfreqlist):
    print(f"""
--- Report for {path_to_book} ---
{number_of_words} were found in the document    
          """)
    for each_dictionary in formatted_charfreqlist:
        if each_dictionary["char"].isalpha():
            print (f"The character {each_dictionary["char"]} was  found {each_dictionary["num"]} times.")
    print("""
--- End Report ---""")

if __name__ == '__main__':
    main()
