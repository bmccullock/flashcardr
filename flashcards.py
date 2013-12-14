# Flashcard Tool
#
# A simple program to study for a test or exam. Feed the program a set of
# questions via a text file and work through them at random.
#
# To Do:
#   Create database to hold question sets...SQLAlchemy?

import random
import json
import os
from flask import Flask, render_template, request, session, g, redirect, \
    abort, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

import models

class Quiz:
    '''Collection of flashcards for study'''

    def __init__(self, quiz_id):
        self.name = models.Quiz.query.get(quiz_id).name
        self.cards = models.Card.query.filter_by(quiz = quiz_id).all()     

    def __repr__(self):
        return '<Quiz object containing %d flashcards>' % len(self.cards)

    def show_all(self):
        for c in self.cards:
            print c

    def get_card(self):
        return random.choice(self.cards)


@app.route('/')
def show_card():
    return render_template('index.html', question_sets = question_sets)

@app.route('/quiz-<int:quiz_id>')
def quiz(quiz_id):    
    quiz = Quiz(quiz_id)
    card = quiz.get_card()
    return render_template('card.html', question = card.question, 
        answer = json.dumps(card.answer), name = quiz.name)

if __name__ == '__main__':
    #working_set = Quiz()
    #working_set.load(questions)
    question_sets = models.Quiz.query.all()
    app.run(debug = True)


