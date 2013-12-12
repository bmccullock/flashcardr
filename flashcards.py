# Flashcard Tool
#
# A simple program to study for a test or exam. Feed the program a set of
# questions via a text file and work through them at random.
#
# To Do:
#   Create database to hold question sets...SQLAlchemy?

import random
import json
from flask import Flask, render_template

app = Flask(__name__)

class Set:
    '''Collection of flashcards for study'''

    def __init__(self):
        self.cards = []

    def __repr__(self):
        return '<Set object containing %d flashcards>' % len(self.cards)

    def load(self, questions_dict):
        for k in iter(questions):
            self.cards.append(Card(self, k, questions[k]))

    def show_all(self):
        for c in self.cards:
            print c

    def get_card(self):
        return random.choice(self.cards)

class Card(object):
    '''A single flashcard with a question and an answer'''

    def __init__(self, card_set, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return '%s >> %s' % (self.question, self.answer)

    def question(self):
        return self.question

    def answer(self):
        return self.answer

questions = {
    'What color is an orange?': 'Orange',
    'How many toes on a sloth?': 'Three',
    'How far is the Earth from the Sun?': '1 A.U.',
    '37 + 15': '52',
    'Spell a C7 chord': 'C-E-G-Bb',
    'What day comes before Saturday?': 'Friday'
}


@app.route('/')
def show_card():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    card = working_set.get_card()
    question = card.question
    answer = card.answer
    return render_template('card.html', question = question, answer = json.dumps(answer))

if __name__ == '__main__':
    working_set = Set()
    working_set.load(questions)
    app.run(debug = True)


