def get_num_words(text):
    
    word_count = 0
    
    for i in text.split():
        word_count += 1
    
    return word_count

def get_num_letters(text):
    
    #letters = ['a','b','c','d','e','f','g','h','i','j','k','l',
    #'m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letters = [chr(i) for i in range(32, 255)]
    #print(letters)
    letters_dict = {}
    letter_count = 0
    
    for i in letters:
        for j in text:
            if j.lower() == i:
                letter_count += 1
        letters_dict[i] = f' {letter_count}'
        letter_count = 0

    return letters_dict