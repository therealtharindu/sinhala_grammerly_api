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


#used to return true if the word is spelled correcly or otherwise false
def is_correctly_spelled(word):
    word = word.lower()
    read_dictionary_file()
    return word in dictionary



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
