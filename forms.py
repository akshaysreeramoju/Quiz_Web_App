from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField

class QuizForm(FlaskForm):
    question = RadioField('', choices=[
        ('quiz.html', 'C'),

        ('quiz1.html', 'Java'),

        ('quiz2.html', 'Python')
    ])
    submit = SubmitField('Submit')