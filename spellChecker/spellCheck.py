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



def read_local_dictionary_file():
    # dictionary = []
    with open("dataset/local_dictionary.text","r",encoding="UTF-8") as f:
        contents = f.read()
        dictionary = list(
            word.lower().replace('\u200d', '')
            for word in contents.splitlines()
        )
    return dictionary
        
def word_in_local(word):
    local_dictionary = read_local_dictionary_file()
    if(word in local_dictionary):
        return 1
    else:
        return 0

#used to return true if the word is spelled correcly or otherwise false
def is_correctly_spelled(word):
    word = word.lower()

    read_dictionary_file()
    word_in_local_dictionary = word_in_local(word)
    # local_dictionary = read_local_dictionary_file()
    
    # return word in dictionary
    word_in_dictionary = searchLib.binarySearch(dictionary,0,len(dictionary)-1,word)
    # word_in_local_dictionary = searchLib.binarySearch(local_dictionary,0,len(local_dictionary)-1,word)


    print(word_in_dictionary)
    print(word_in_local_dictionary)

    if (word_in_dictionary == 1 or word_in_local_dictionary == 1):
        
        return True
    else:
        print('not found in both ')
        return False



#sinhala tokenized word
def readSinhalaWordList():
  sinhala_corpus = []
  with open('dataset/sinhala_list.text',encoding='UTF-8') as file:
    for word in file:
      word = word.strip()
      removeUnicodeError = word.replace('\u200d', '')
      sinhala_corpus.append(removeUnicodeError)
    return sinhala_corpus


#remove unicode error in wordlist by removing \u200d in insert word
def removeUnicodeError(word):
    removeUnicodeError = word.replace('\u200d', '')
    return removeUnicodeError
