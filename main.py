def main():
    
    letter_list = []
    file_contents = read_file_path("books/frankenstein.txt")
    word_count = count_words(file_contents)
    letter_count = count_letters(file_contents)
    letter_data = aggregate_letter_data(letter_count)
    
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document \n \n")
    print_letter_data(letter_data)
    print(f"--- End report ---")

def read_file_path(path):
    
    with open(path) as f:
        
        return f.read()

def count_words(text):
    
    word_count = 0
    
    for i in text.split():
        word_count += 1
    
    return word_count

def count_letters(text):
    
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l',
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letters_dict = {}
    letter_count = 0
    
    for i in letters:
        for j in text:
            if j.lower() == i:
                letter_count += 1
        letters_dict[i] = letter_count
        letter_count = 0

    return letters_dict

def aggregate_letter_data(dict):
    dict_list = []
    
    for i in dict:
        dict_list.append({"letter": i, "count": dict[i]})
    
    dict_list.sort(reverse=True, key=sort_on)

    return dict_list

def print_letter_data(list):

    for i in list:
        print(f"The '{i["letter"]}' character was found {i["count"]} times\n")

def sort_on(dict):
    return dict["count"]

main()


