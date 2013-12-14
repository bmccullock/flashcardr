from flashcards import db

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    cards = db.relationship('Card', backref = 'quiz_set', lazy = 'dynamic')

class Card(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    quiz = db.Column(db.Integer, db.ForeignKey('quiz.id'))
    question = db.Column(db.String())
    answer = db.Column(db.String())


