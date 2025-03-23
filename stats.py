
def get_book_text(path):
    with open (path) as f:
        return f.read()


def get_num_words(path):	
    text = get_book_text(path)
    num_words = text.split() # splits the text into seperate words as strings
    word_number = len(num_words)
    return word_number

def num_letters(path):	
    text = get_book_text(path)
    letters_dict = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in letters_dict:
            letters_dict[lower_char] = 1
        else:
            letters_dict[lower_char] += 1
    return letters_dict

def sort(letters_dict):
    letters_list = []
    for char, count in letters_dict.items():
        letters_list.append({"char": char, "count": count})
    
    def sort_on(dict):
        return dict["count"]

    letters_list.sort(reverse=True, key=sort_on)
    return letters_list
