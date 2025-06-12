import sys
from stats import get_num_words, get_num_letters

def main():
    
    letter_list = []
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    file_contents = read_file_path(sys.argv[1])
    word_count = get_num_words(file_contents)
    letter_count = get_num_letters(file_contents)
    letter_data = aggregate_letter_data(letter_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_letter_data(letter_data)
    print("============= END ===============")

def read_file_path(path):
    
    with open(path) as f:
        
        return f.read()

def aggregate_letter_data(dict):
    dict_list = []
    
    for i in dict:
        dict_list.append({"letter": i, "count": dict[i]})
    
    dict_list.sort(reverse=True, key=sort_on)

    return dict_list

def print_letter_data(list):

    for i in list:
        print(f"{i["letter"]}:{i["count"]}")

def sort_on(dict):
    return int(dict["count"])

main()


