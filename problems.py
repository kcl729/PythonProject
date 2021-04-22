import random 
from problems_and_answers import problem_dictionary

global correct_answers_count
correct_answers_count = 0

def generate_problem():
    """generates and returns a random problem statement from the problem/answer dictionary
    random_problem_key is equal to a random key from the problem dictionary
    problem_statement is equal to the problem obtained from the first list value of random_problem_key"""
    global random_problem_key
    random_problem_key = random.choice(list(problem_dictionary.keys()))
    problem_statement =  problem_dictionary[random_problem_key][0]   
    return problem_statement 

def reset_count(correct_answers_count):
    """ reset the correct_answers_count after a session has ended so that user may do another session
    returns: None -- function just edits the global variable""" 
    correct_answers_count = 0
    return None

def check_answer(answer):
    """ check user's answer against the correct answer in the dictionary 
    User's answer is stored as the argument answer
    Actual answer is stored as the variable solution, obtained as the second list value of random_problem_key
    returns: a string that explains whether or not the answer was right and what the correct answer would be.  """
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
    """function that displays the user's results at the end of a practice session & resets it to 0 in case the user wants to start another session
    returns string with message to share user statistics"""
    global correct_answers_count
    rightanswers = correct_answers_count
    results = f'You got a total of {rightanswers} questions correct.'
    correct_answers_count = 0
    return results 

def q_req(count):
    """function that processes the index form that indicates how many questions user want to do in one session
    count is an argument that stores the user's input from the index form. This function translates it from string to the integer total_questions.
    returns integer"""
    if count == "five":
        total_questions = 5
    elif count == "ten":
        total_questions = 10
    else:
        total_questions = 15
    return total_questions