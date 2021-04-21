import random 
from problems_and_answers import problem_dictionary

global correct_answers_count
correct_answers_count = 0

def generate_problem():
    global random_problem_key
    random_problem_key = random.choice(list(problem_dictionary.keys()))
    problem_statement =  problem_dictionary[random_problem_key][0]   
    return problem_statement 

def reset_count(correct_answers_count):
    correct_answers_count = 0
    return None

def check_answer(answer):
    solution = problem_dictionary[random_problem_key][1]
    # global questions_count
    # questions_count += 1
    if solution == answer:
        global correct_answers_count
        correct_answers_count += 1
        reply = f'Correct!'
    else: 
        reply = f'Incorrect. The correct answer is {problem_dictionary[random_problem_key][1]}'
    del problem_dictionary[random_problem_key]
    return reply

def show_results():
    global correct_answers_count
    rightanswers = correct_answers_count
    results = f'You got a total of {rightanswers} questions correct.'
    correct_answers_count = 0
    return results 

def q_req(count):
    if count == "five":
        total_questions = 5
    elif count == "ten":
        total_questions = 10
    else:
        total_questions = 15
    return total_questions