import random

#Problem 1 Data
p1_net_income_year1 = random.randrange(100,500,50)                                      
p1_revenue_year1 = random.randrange(500,1000,50)
p1_revenue_year2 = random.randint(1,10)  

#Problem 2 Data
p2_number_of_employees = random.randrange(20000,60000,1000)                                      
p2_number_of_partners = random.randrange(200,600,50) 

#Problem 3 Data
p3_percent_buyers = random.randrange(60,100,5)
p3_percent_sneaker_buyers = random.randrange(10,50,5)

#problem dictionary
problem_dictionary = {'P1':[f'Facebook had net income of ${p1_net_income_year1} million in 2009 on revenue of ${p1_revenue_year1} million. Figures for 2010 weren\'t disclosed yet, but analysts have said the company\'s revenue in 2010 could be as much as ${p1_revenue_year2} billion, fueled by advertising growth. If Facebook maintained the same profit margin as in 2009, what would be their net income in 2010? (round to one decimal)',round(((p1_net_income_year1/p1_revenue_year1)*p1_revenue_year2*1000000000),1)],'P2':[f'About {p2_number_of_partners} of Goldman Sachs (NYSE:GS)\'s roughly {p2_number_of_employees} employees have the title of partner, what\'s the percentage of partners among all Goldman Sachs employees?',round((p2_number_of_partners/p2_number_of_employees)*100,1)],'P3':[f' The manager of an clothing store in Boston needed to calculate the percentage of customers who purchase sneakers. Upon completing her survey, she noticed that {p3_percent_buyers}% of the people that entered her store purchased an item. Of those customers, {p3_percent_sneaker_buyers}% percent purchased sneakers. What percent of the people that entered the clothing store purchased sneakers? (round to nearest integer)',round(p3_percent_buyers*(p3_percent_sneaker_buyers/100),0)]}

def math_tracker():
    number_of_questions_so_far = 0
    number_correct_answers = 0                                                        
    while number_of_questions_so_far < 10:
        random_problem()
def random_problem():
    random_problem = random.choice(list(problem_dictionary.keys()))
    number_of_questions_so_far += 1 
    correct_answer = problem_dictionary[random_problem][1]
    return random_problem                                                                                            
    # problem = input(problem_dictionary[random_problem][0])                  
    # answer = float(problem)   
    
    # if answer == correct_answer:                                            
    #     number_correct_answers += 1
    #     del problem_dictionary[random_problem]     
    #     return f'Correct! You have a total of {number_correct_answers} correct answers. You have worked on {number_of_questions_so_far} problems so far'   
    # else:                                                                   
    #     del problem_dictionary[random_problem] 
    #     return f'Wrong. The correct answer is {correct_answer}. You have a total of {number_correct_answers} correct answers. You have worked on {number_of_questions_so_far} problems so far'   
                                           
                                                                                  
