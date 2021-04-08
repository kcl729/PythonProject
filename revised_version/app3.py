from flask import Flask
from flask import request
# from mbta_helper import find_stop_near
from flask import render_template
# need help with importing dictionary and generate_problem function from problems.py
from myDict import problem_dictionary
from problems import generate_problem

app = Flask(__name__)

# @app.route('/')
# def main_page():
#     return render_template('index.html')

global number_correct_answers = 0
global number_of_questions_so_far = 0


# startpage: 
@app.route('/')
def display_problem():
    # execute the function that take a random key from the dictionary
    global key = problems.generate_problem()
    problem_statement = problem_dictionary[key][0]
    # return the index html 
    return render_template('index.html')

@app.route('/', methods=["GET", "POST"])
def check_answer():
    if request.method == "POST":
        solution = problem_dictionary[key][1]
        answer = float(request.form['math_answer'])        
        number_of_questions_so_far += 1
        if solution == answer:
            number_correct_answers += 1 
            reply = f'Correct! You have a total of {number_correct_answers} correct answers. You have worked on {number_of_questions_so_far} problems so far'
        else: 
            reply = f'Wrong. The correct answer is {solution}. You have a total of {number_correct_answers} correct answers. You have worked on {number_of_questions_so_far} problems so far'
        del problem_dictionary[key]
        return render_template('checkanswer.html')

if __name__ == "__main__":
    app.run(debug=True)
