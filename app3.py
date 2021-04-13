from flask import Flask
from flask import request
import random
# from mbta_helper import find_stop_near
from flask import render_template
from problems import check_answer, generate_problem
# need help with importing dictionary and generate_problem function from problems.py
from problems_and_answers import problem_dictionary

global correct_answers_count
correct_answers_count = 0
global questions_count 
questions_count = 0

def generate_problem():
    global random_problem_key
    random_problem_key = random.choice(list(problem_dictionary.keys()))
    problem_statement =  problem_dictionary[random_problem_key][0]   
    return problem_statement 

def check_answer(answer):
    solution = problem_dictionary[random_problem_key][1]
    global questions_count 
    questions_count += 1
    if solution == answer:
        global correct_answers_count
        correct_answers_count += 1
        reply = f'Correct! You have a total of {correct_answers_count} correct answers. You have worked on {questions_count} problems so far'
    else: 
        reply = f'Wrong. The correct answer is {problem_dictionary[random_problem_key][1]}. You have a total of {correct_answers_count} correct answers. You have worked on {questions_count} problems so far'
    del problem_dictionary[random_problem_key]
    return reply
app = Flask(__name__)

# startpage: 
@app.route('/')
def get_started():
    return render_template('index.html')

@app.route('/', methods=["GET", "POST"])
def display_problem():
    problem_statement = generate_problem() 
    return render_template('questions.html', problem_statement=problem_statement)

@app.route('/', methods=["GET", "POST"])
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
