#from tokenization.tokenizer import SinhalaWordTokenizer
# from binarysearch import sinhalaTokenizedWord,findTheWord,searching,removeUnicodeErrorWord
from spellChecker import is_correctly_spelled,read_dictionary_file,readSinhalaWordList,removeUnicodeError
from misspelledwords.regularMisspelled import correct_misspelled_word
from search import  get_close_words
from add_to_local_dictionary import add_to_local_dictionary
from flask import Flask, jsonify, request,json
from flask_restful import Api, Resource
from flask_cors import CORS
dictionary = set()
import sys
import spellChecker

app = Flask(__name__)
CORS(app)
api = Api(app)

# @app.route("/")
# def home():
#     return "Hello, world!"


#spell checking input from the post request
@app.route('/api/spellchecking',methods = ['POST'])
def index():
    content = request.get_json()
    singleWord = content['word']
    removedUnicodeError = removeUnicodeError(singleWord)
    # print(readSinhalaWordList()) # to know whether this is corrected.
    return jsonify(is_correctly_spelled(removedUnicodeError))

@app.route('/api/misspelledword', methods = ['POST'])
def corrected_word():
    content = request.get_json()
    word = content['word']
    corrected_word = correct_misspelled_word(word)

    return jsonify(corrected_word)

@app.route('/api/closewords', methods = ['POST'])
def list_of_close_words():
    content = request.get_json()
    word = content['word']
    close_words = get_close_words(word)
    

    return jsonify(close_words)

@app.route('/api/add_to_local_dictionary', methods = ['POST'])
def add_to_local():
    content = request.get_json()
    word = content['word']
    added_word = add_to_local_dictionary(word)
    

    return jsonify(added_word)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)