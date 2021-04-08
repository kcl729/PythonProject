import random

#Problem 1 Data
p1_net_income_year1 = random.randrange(100,500,50)                                      
p1_revenue_year1 = random.randrange(500,1000,50)
p1_revenue_year2 = random.randint(1,10)  

#Problem 2 Data
p2_number_of_employees = random.randrange(20000,60000,1000)                                      
p2_number_of_partners = random.randrange(200,600,50) 

problem_dictionary = {'P1':f'Facebook had net income of ${p1_net_income_year1} million in 2009 on revenue of ${p1_revenue_year1} million. Figures for 2010 weren\'t disclosed yet, but analysts have said the company\'s revenue in 2010 could be as much as ${p1_revenue_year2} billion, fueled by advertising growth. If Facebook maintained the same profit margin as in 2009, what would be their net income in 2010? (round to one decimal)','P2':f'About {p2_number_of_partners} of Goldman Sachs (NYSE:GS)\'s roughly {p2_number_of_employees} employees have the title of partner, what\'s the percentage of partners among all Goldman Sachs employees?'}

def math_problem_practice():
    number_of_questions_so_far = 0
    number_correct_answers = 0                                                        
    while number_of_questions_so_far < 10:                                                 
        random_problem = random.choice(list(problem_dictionary.keys()))
        if random_problem == 'P1':                                                                                              
            problem = input(problem_dictionary['P1'])
            correct_answer = round(((p1_net_income_year1/p1_revenue_year1)*p1_revenue_year2*1000000000),1)                   
            answer = float(problem)                                                   
            if answer == correct_answer:                                            
                number_correct_answers += 1                            
                print(f'Correct! You have a total of {number_correct_answers} correct answers')        
            else:                                                                   
                print(f'Wrong. The correct answer is {correct_answer}')
            del problem_dictionary['P1']                                                             
        elif random_problem == 'P2':                                                                                                                 
            problem = input(problem_dictionary['P2'])
            correct_answer = round((p2_number_of_partners/p2_number_of_employees)*100,1)                   
            answer = float(problem)                                                   
            if answer == correct_answer:                                            
                number_correct_answers += 1                            
                print(f'Correct! You have a total of {number_correct_answers} correct answers')        
            else:                                                                   
                print(f'Wrong. The correct answer is {correct_answer}') 
            del problem_dictionary['P2']      
        number_of_questions_so_far += 1 
        #we keep adding problems here...                                                                                                   
    print(f'Congratulations! You did a great job. You had {number_correct_answers}')      

math_problem_practice()