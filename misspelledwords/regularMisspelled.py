#create a dictionary with misspelled words
common_misspelled_words = {
    'sch':'school',
    'scho':'school',
    'schoo': 'school',
    'schol':'school',
    'scool':'school',
    'skool':'school',
    'skoo':'school',
    'tha':'the',
    'thw':'the',
    'th':'the'
    
}
def correct_misspelled_word(word):
  return common_misspelled_words[word]


    