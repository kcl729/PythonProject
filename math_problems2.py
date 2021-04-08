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

#Problem 4 Data
p4_single_bag_price = random.randrange(1,3,1)
p4_tenpack_bag_price = random.randrange(5,10,1)

#Problem 5 Data
p5_number_large_desks = random.randrange(50,100,1)
p5_number_small_desks = random.randrange(1,50,1)

#Problem 6 Data
p6_number_burguers_sold_2019 = random.randrange(2_000_000,5_000_000,1000)
p6_percentage_increase = random.randrange(10,100,10)

#Problem 7 Data
p7_initial_price = random.randrange(50,100,5) 
p7_percentage_increase = random.randrange(2,10,1)
p7_discount = random.randrange(10,30,1)

#problem dictionary
problem_dictionary = {'P1':[f'Facebook had net income of ${p1_net_income_year1} million in 2009 on revenue of ${p1_revenue_year1} million. Figures for 2010 weren\'t disclosed yet, but analysts have said the company\'s revenue in 2010 could be as much as ${p1_revenue_year2} billion, fueled by advertising growth. If Facebook maintained the same profit margin as in 2009, what would be their net income in 2010? (round to one decimal)',round(((p1_net_income_year1/p1_revenue_year1)*p1_revenue_year2*1000000000),1)],'P2':[f'About {p2_number_of_partners} of Goldman Sachs (NYSE:GS)\'s roughly {p2_number_of_employees} employees have the title of partner, what\'s the percentage of partners among all Goldman Sachs employees?',round((p2_number_of_partners/p2_number_of_employees)*100,1)],'P3':[f' The manager of an clothing store in Boston needed to calculate the percentage of customers who purchase sneakers. Upon completing her survey, she noticed that {p3_percent_buyers}% of the people that entered her store purchased an item. Of those customers, {p3_percent_sneaker_buyers}% percent purchased sneakers. What percent of the people that entered the clothing store purchased sneakers? (round to nearest integer)',round(p3_percent_buyers*(p3_percent_sneaker_buyers/100),0)],'P4':[f'The price of a bag of chips is ${p4_single_bag_price}. The price of a ten pack of the same bag of chips is ${p4_tenpack_bag_price}. The ten pack of bag chips is what percentage cheaper than purchasing ten bag of chips individually? (round to nearest integer percentage)',round(((1-((p4_tenpack_bag_price/10)/p4_single_bag_price))*100),0)],'P5':[f'An office manager purchased {p5_number_large_desks} large desks and {p5_number_small_desks} small desks. If the price of a large desk is three times the price of a small desk, what percent of the total cost was the cost of all the small desks?', round(((p5_number_small_desks/(p5_number_small_desks + 3*p5_number_large_desks))*100),0)],'P6':[f'The number of plant-based burguers sold in Boston during 2019 was {p6_number_burguers_sold_2019}; up {p6_percentage_increase}% from three years before. How many burguers were sold three years before 2019?',round((p6_number_burguers_sold_2019/(1+p6_percentage_increase/100)),0)], 'P7':[f'A chair in Wayfair\'s webiste was priced at ${p7_initial_price}. The marketing manager thought he could get more money for the chair, so he increased its price by {p7_percentage_increase}%. After a week, the chair had not been sold. The manager then discounted the new price by {p7_discount}%, and the chair was finally sold. For how much was the chair sold? (round to nearest percentage integer)',round((p7_initial_price*(1+(p7_percentage_increase/100))*(1-(p7_discount/100))),0)]}


#function to run practice problems from dictionary
def math_problem_practice():
    number_of_questions_so_far = 0
    number_correct_answers = 0                                                        
    while number_of_questions_so_far < 10:                                                 
        random_problem = random.choice(list(problem_dictionary.keys()))
        number_of_questions_so_far += 1                                                                                             
        problem = input(problem_dictionary[random_problem][0])                  
        answer = float(problem)   
        correct_answer = problem_dictionary[random_problem][1]                                            
        if answer == correct_answer:                                            
            number_correct_answers += 1                            
            print(f'Correct! You have a total of {number_correct_answers} correct answers. You have worked on {number_of_questions_so_far} problems so far')        
        else:                                                                   
            print(f'Wrong. The correct answer is {correct_answer}. You have a total of {number_correct_answers} correct answers. You have worked on {number_of_questions_so_far} problems so far')
        del problem_dictionary[random_problem]                                                                                                                                                                   
    print(f'Congratulations! You did a great job. You had {number_correct_answers}')      




math_problem_practice()