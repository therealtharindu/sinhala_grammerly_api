
from os import write




def read_dictionary_file():

    with open("dataset/local_dictionary.text","r",encoding="UTF-8") as f:
        content = f.read()
        word_list = content.splitlines()
    return word_list

# check herer ================
def add_to_local_dictionary(word):

    dictionary = read_dictionary_file()
    


    if word in dictionary:
       return False
    else:
        with open("dataset/local_dictionary.text","a",encoding="UTF-8") as w:
            w.write(word +"\n")
        return True

    
        

# add_to_local_dictionary("රටටරටට")
