import random 
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