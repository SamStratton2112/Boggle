from flask import Flask, request, render_template, jsonify, session, redirect, flash, current_app
from boggle import Boggle
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config["SECRET_KEY"] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

boggle_game = Boggle()



@app.route('/', methods=['GET'])
def start_page():
    """ shows new boggle board"""
    board = boggle_game.make_board()
    session['board'] = board
    session['wordsList'] = []
    wordsList = session['wordsList']
    session['score']= 0
    score = session['score']
    return render_template('start.html', board = board, score = score, wordsList = wordsList) 

@app.route('/validate', methods=['GET'])
def post_word():
    """ shows new boggle board"""
    word = request.args['word']
    board = session['board']
    validWord = boggle_game.check_valid_word(board,word)
    score = session['score']
    wordsList = session['wordsList']
    if validWord == 'ok':
        wordsList.append(word)
        print('WORDSLIST', wordsList)
        session['wordsList'] = wordsList
        addPoints = len(word)
        score+= addPoints
        session['score'] = score
    print(session)
    return jsonify({ 'result' : validWord, 'score' : score})





# I've spent too much time on this so I'm moving on  