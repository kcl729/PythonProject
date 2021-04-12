from flask import Flask
from flask import request
import random
# from mbta_helper import find_stop_near
from flask import render_template
# need help with importing dictionary and generate_problem function from problems.py

app = Flask(__name__)

# to do:
# import the functions from python file (both generate_problem, and check_answer)
# add css to html pages

# startpage: 
@app.route('/')
def display_problem():
    problem_statement = generate_problem() 
    return render_template('index.html', problem_statement=problem_statement)

@app.route('/', methods=["GET", "POST"])
def reply():
    if request.method == "POST":
        answer = float(request.form['math_answer'])
        reply = check_answer(answer)     
    return render_template('checkanswer.html', reply=reply)

if __name__ == "__main__":
    app.run(debug=True)
