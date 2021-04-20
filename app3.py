from flask import Flask
from flask import request
import random
# from mbta_helper import find_stop_near
from flask import render_template
from problems import check_answer, generate_problem
# need help with importing dictionary and generate_problem function from problems.py
from problems_and_answers import problem_dictionary

app = Flask(__name__)

global total_questions
global correct_answers_count
correct_answers_count = 0
global questions_count 
questions_count = 0

# startpage: 
@app.route('/')
def get_started():
    return render_template('index.html')

# startpage data processing
@app.route('/', methods=["GET", "POST"])
def questions_number():
    if request.method == "POST":
        count = request.form.get('count')
        global total_questions
        if count == "ten":
            total_questions = 10
        elif count == "twenty":
            total_questions = 20
        else:
            total_questions = 30
        return render_template('welcome.html', total_questions=total_questions)

# actual app:
@app.route('/questions')
def show_problem():
    while questions_count < total_questions:
        problem_statement = generate_problem() 
        return render_template('questions.html', problem_statement=problem_statement)
    return render_template('end.html')
    
# check answers:
@app.route('/questions', methods=["GET", "POST"])  
def reply():
    try:
        if request.method == "POST":
            answer = float(request.form['math_answer'])
            reply = check_answer(answer)     
        return render_template('checkanswer.html', reply=reply)
    except ValueError:
        return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)
