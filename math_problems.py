import random
def math_problem_practice():
    number_of_questions_so_far = 0
    number_correct_answers = 0                                                        
    while number_of_questions_so_far < 10:                                                 
        random_problem = random.choice(['P1', 'P2']) 
        if random_problem == 'P1':
            number_of_questions_so_far += 1                                          
            net_income_year1 = random.randrange(100,500,50)                                      
            revenue_year1 = random.randrange(500,1000,50)
            revenue_year2 = random.randint(1,10)                                                                              
            problem = input(f'Facebook had net income of ${net_income_year1} million in 2009 on revenue of ${revenue_year1} million. Figures for 2010 weren\'t disclosed yet, but analysts have said the company\'s revenue in 2010 could be as much as ${revenue_year2} billion, fueled by advertising growth. If Facebook maintained the same profit margin as in 2009, what would be their net income in 2010? (round to one decimal)')
            correct_answer = round(((net_income_year1/revenue_year1)*revenue_year2*1000000000),1)                   
            answer = float(problem)                                                   
            if answer == correct_answer:                                            
                number_correct_answers += 1                            
                print(f'Correct! You have a total of {number_correct_answers} correct answers')        
            else:                                                                   
                print(f'Wrong. The correct answer is {correct_answer}')                                                             
        elif random_problem == 'P2':                                      
            number_of_employees = random.randrange(20000,60000,1000)                                      
            number_of_partners = random.randrange(200,600,50)                                                                            
            problem = input(f'About {number_of_partners} of Goldman Sachs (NYSE:GS)\'s roughly {number_of_employees} employees have the title of partner, what\'s the percentage of partners among all Goldman Sachs employees?')
            correct_answer = round((number_of_partners/number_of_employees)*100,1)                   
            answer = float(problem)                                                   
            if answer == correct_answer:                                            
                number_correct_answers += 1                            
                print(f'Correct! You have a total of {number_correct_answers} correct answers')        
            else:                                                                   
                print(f'Wrong. The correct answer is {correct_answer}')   
        #we keep adding problems here...                                                                                                   
    print(f'Congratulations! You did a great job. You had {number_correct_answers}')      

math_problem_practice()