#from tokenization.tokenizer import SinhalaWordTokenizer
# from binarysearch import sinhalaTokenizedWord,findTheWord,searching,removeUnicodeErrorWord
from spellChecker import is_correctly_spelled,read_dictionary_file,readSinhalaWordList,removeUnicodeError
from misspelledwords.regularMisspelled import correct_misspelled_word
from search import  get_close_words
from add_to_local_dictionary import add_to_local_dictionary
from flask import Flask, jsonify, request,json ,render_template,url_for, session,redirect
from authlib.integrations.flask_client import OAuth
import os
from datetime import timedelta
from flask_restful import Api, Resource
from flask_cors import CORS
dictionary = set()
import sys
import spellChecker
from flask_sqlalchemy import SQLAlchemy
# decorator for routes that should be accessible only by logged in users
from auth_decorator import login_required

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)



CORS(app)
api = Api(app)

#sql connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='', server='localhost', database='grammerly')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)



# Session config
app.secret_key = os.getenv("APP_SECRET_KEY")


app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

# oAuth Setup
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
)




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)

    def __init__(self,username,email):
        self.username = username
        self.email = email

# @app.route("/")
# def home():
#     return render_template('index.html')

@app.route('/')
@login_required
def hello_world():
    # email = dict(session)['profile']['email']
    # return f'Hello, you are logged in as {email}!'
     user_name = request.args['user_name']
     return render_template('index.html',user_name = user_name)


@app.route('/login')
def login():
    google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')  # create the google oauth client
    token = google.authorize_access_token()  # Access token from google (needed to get user info)
    resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    user_info = resp.json()
    user_name = user_info["name"]
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    print(f'user ID : {user_info["id"]}')
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    session['profile'] = user_info
    session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed

    



    return redirect(url_for('.hello_world',user_name = user_name))


@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')


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
    