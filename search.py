# import difflib
# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process
import searchLib

dictionary = list()

def read_dictionary_file():
    global dictionary

    if dictionary:
        return 

    with open("dataset/sinhala_list2.text","r",encoding="UTF-8") as f:
        contents = f.read()
        dictionary = list(
            word.lower().replace('\u200d', '')
            for word in contents.splitlines()
        )
        


def get_close_words(word):
    read_dictionary_file()
    
    wordindex = searchLib.binarySearch(dictionary,0,len(dictionary)-1,word)
    wordlist= list()
    if wordindex == 1:
        return False
    else:
       wordlist.append(dictionary[wordindex])
       wordlist.append(dictionary[wordindex-1])
       wordlist.append(dictionary[wordindex-2])
       wordlist.append(dictionary[wordindex+1])
       wordlist.append(dictionary[wordindex+2])
    return wordlist
    

# get_close_words("කොරෝනා")

# def get_close_words(word):
#     read_dictionary_file()
#     if word in dictionary:
#         return False
#     else:
#         wordlist = difflib.get_close_matches(word, dictionary,n=5)
#         # processedwordlist = process.extract(word, dictionary, limit=5)

#         # wordlist = [tuplelist[0] for tuplelist in processedwordlist]
#         return wordlist








