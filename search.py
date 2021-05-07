import difflib

dictionary = set()

def read_dictionary_file():
    global dictionary

    if dictionary:
        return 

    with open("dataset/sinhala_list.text","r",encoding="UTF-8") as f:
        contents = f.read()
        dictionary = set(
            word.lower().replace('\u200d', '')
            for word in contents.splitlines()
        )
        
def get_close_words(word):
    read_dictionary_file()
    if word in dictionary:
        return False
    else:
        wordlist = difflib.get_close_matches(word, dictionary,n=5)
        return wordlist
    
    
# get_close_words('අකුස')



# words = ['රසායනික','රසායන','රසායනාගාරය','පාසල','පාසලක්','පාසලේ']
# wordlist = difflib.get_close_matches('පාස', words)

# if not wordlist:
#     print('Not found in the List')
# else:
#     print(wordlist)








