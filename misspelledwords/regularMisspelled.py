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
    'th':'the',
    'ප්‍රබුද්':'ප්‍රබුද්ධ',
    'ප්‍රබද්ධ':'ප්‍රබුද්ධ',
    'ප්‍බද්ධ':'ප්‍රබුද්ධ',
    'ප්‍රබුද්ධ':'ප්‍රබුද්ධ',
    'අධ්‍පනය':'අධ්‍යාපනය',
    'අධ්‍යානය':'අධ්‍යාපනය',
    'අධ්‍යාපය':'අධ්‍යාපනය',
    'ජයවර්ධනපු':'ජයවර්ධනපුර',
    'ජයවරධනපුර':'ජයවර්ධනපුර',
    'ජයවර්ධනපර':'ජයවර්ධනපුර',
    'ජවර්ධනපුර':'ජයවර්ධනපුර',
    'තුවා':'තුවාල',
    'රසායනාගාර':'රසායනාගර',
    'රසායනාගා':'රසායනාගාර',
    'රසායගාර':'රසායනාගාර'
    
}
def correct_misspelled_word(word):
  if word in common_misspelled_words:
    return common_misspelled_words[word]
  else:
    return False
  



    