from flask import Flask,render_template,url_for,request,redirect,flash,session
from forms import QuizForm
from flask_mysqldb import *


app = Flask(__name__)

app.config['SECRET_KEY'] = 'your-secret-key'

@app.route("/")
def home():
   return render_template('index.html')

@app.route("/index")
def index():
   return render_template('index.html')


@app.route("/register")
def register():
   return render_template('register.html')

@app.route("/codeselection",methods=['post'])
def codeselection():
     form = QuizForm()
     if form.validate_on_submit():
        # Process the form data
        selected_option = form.question.data
        # Perform your logic with the selected option
        return render_template(selected_option)
     return render_template('codeselection.html',form=form)

@app.route('/result', methods=['POST'])
def result():
    # Get the quiz score from localStorage
    quiz_score = request.form['quizScore']
    return render_template('result.html', score=quiz_score)

@app.route('/index', methods=['POST'])
def add():
   return render_template('index.html')

@app.route('/codeselection', methods=['POST'])
def rose():
   return render_template('codeselection.html')


if __name__=="__main__":
    app.run(debug=True)



