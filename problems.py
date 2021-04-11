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

#Problem 8 Data
p8_investment = random.randrange(100000,200000,300000)
p8_rev = random.randrange(290, 340, 505)
p8_cost = random.randrange(100,200,230)

#Problem 9 Data
p9_investment = random.randrange(500000,1000000,15000000)
p9_growthrate = random.randrange(20,30,40)
p9_periods = random.randrange(2,3,4)
p = 0 
p9_endamount = p9_investment 
while p < p9_periods:
    p9_endamount = p9_endamount * p9_growthrate
    p += 1

#problem 10 data
p10_percentage = random.randrange(13,17,21)
p10_quantity = random.randrange(790000, 815000, 950000)

# problem 11 data
p11_fixedcost = random.randrange(3000000, 3200000, 3450000)
p11_units = random.randrange(175000, 450000, 515000)

# problem 12 data 
p12_rev = random.randrange(250000, 300000, 350000)
p12_percentageincr = random.randrange(23,28,32)
p12_solution = p12_rev + (1+(p12_percentageincr/100))*p12_rev

# problem 13 data
p13_output = random.randrange(120000,145000,152000)
p13_employees = random.randrange(55,65,75)

# problem 14
p14_perc = random.randrange(10,12,14)
p14_sales = random.randrange(130000000,145000000,151000000)

# problem 15
p15_invest = random.randrange(850000,1050000,1100000)
p15_cost = random.randrange(100,150,200)
p15_price = random.randrange(250,300,350)

# problem 16
p16_currentrev = random.randrange(1000000,1500000,2000000)
p16_y1growth = random.randrange(3,4,5)
p16_y2growth = random.randrange(5,6,7)
p16_y3growth = random.randrange(2,5,6)
p16_y1rev = p16_currentrev * (1+p16_y1growth/100)
p16_y2rev = p16_y1rev * (1+p16_y2growth/100)
p16_solution = p16_y2rev * (1+p16_y3growth/100)

# problem 17
p17_rev = random.randrange(1000000,1500000,2000000)
p17_profitmargin = random.randrange(9,11,13)
p17_costreductionperc = random.randrange(10,20,30)
p17_costs = (100-p17_profitmargin)/100*p17_rev
p17_solution = p17_costs * ((100-p17_costreductionperc)/100)

#Problem 18
p18_monday_visitors = random.randrange(100,1000,50)
p18_answer = p18_monday_visitors*3**4

#Problem 19
p19_number_hours_worked_week1 = random.randrange(15,40,1)
p19_money_made_week1 = random.randrange(110,150,1)
p19_number_hours_worked_week2 = random.randrange(10,45,1)
p19_answer = (p19_money_made_week1/p19_number_hours_worked_week1)*p19_number_hours_worked_week2

#Problem 20
p20_domain_name_cost = random.randrange(900,3000,50)
p20_it_cost = random.randrange(12000,30000,100)
p20_marketing_cost = random.randrange(7000,20000,100)
p20_price = random.randrange(50,150,5)
p20_answer = (p20_domain_name_cost+p20_it_cost+p20_marketing_cost)/p20_price

#problem dictionary
problem_dictionary = {
'P1':[f'Facebook had net income of ${p1_net_income_year1} million in 2009 on revenue of ${p1_revenue_year1} million. Figures for 2010 weren\'t disclosed yet, but analysts have said the company\'s revenue in 2010 could be as much as ${p1_revenue_year2} billion, fueled by advertising growth. If Facebook maintained the same profit margin as in 2009, what would be their net income in 2010? (round to one decimal)',round(((p1_net_income_year1/p1_revenue_year1)*p1_revenue_year2*1000000000),1)],
'P2':[f'About {p2_number_of_partners} of Goldman Sachs (NYSE:GS)\'s roughly {p2_number_of_employees} employees have the title of partner, what\'s the percentage of partners among all Goldman Sachs employees?',round((p2_number_of_partners/p2_number_of_employees)*100,1)],
'P3':[f' The manager of an clothing store in Boston needed to calculate the percentage of customers who purchase sneakers. Upon completing her survey, she noticed that {p3_percent_buyers}% of the people that entered her store purchased an item. Of those customers, {p3_percent_sneaker_buyers}% percent purchased sneakers. What percent of the people that entered the clothing store purchased sneakers? (round to nearest integer)',round(p3_percent_buyers*(p3_percent_sneaker_buyers/100),0)],
'P4':[f'The price of a bag of chips is ${p4_single_bag_price}. The price of a ten pack of the same bag of chips is ${p4_tenpack_bag_price}. The ten pack of bag chips is what percentage cheaper than purchasing ten bag of chips individually? (round to nearest integer percentage)',round(((1-((p4_tenpack_bag_price/10)/p4_single_bag_price))*100),0)],
'P5':[f'An office manager purchased {p5_number_large_desks} large desks and {p5_number_small_desks} small desks. If the price of a large desk is three times the price of a small desk, what percent of the total cost was the cost of all the small desks?', round(((p5_number_small_desks/(p5_number_small_desks + 3*p5_number_large_desks))*100),0)],
'P6':[f'The number of plant-based burguers sold in Boston during 2019 was {p6_number_burguers_sold_2019}; up {p6_percentage_increase}% from three years before. How many burguers were sold three years before 2019?',round((p6_number_burguers_sold_2019/(1+p6_percentage_increase/100)),0)], 
'P7':[f'A chair in Wayfair\'s webiste was priced at ${p7_initial_price}. The marketing manager thought he could get more money for the chair, so he increased its price by {p7_percentage_increase}%. After a week, the chair had not been sold. The manager then discounted the new price by {p7_discount}%, and the chair was finally sold. For how much was the chair sold? (round to nearest percentage integer)',round((p7_initial_price*(1+(p7_percentage_increase/100))*(1-(p7_discount/100))),0)], 
'P8':[f'What is the breakeven quantity for a business that required an initial investment of {p8_investment}, where each unit brings in {p8_rev} of revenue but each unit costs {p8_cost}?', round(p8_investment/(p8_rev-p8_cost))], 
'P9':[f'What is the expected NPV for an investment of {p9_investment}, where the annual growth rate is expected to be {p9_growthrate} after {p9_periods}?', round(p9_endamount)], 
'P10':[f'What is the addressable market size for company A if they want to reach {p10_percentage} of a total of {p10_quantity}', round((p10_percentage)/100*p10_quantity)], 
'P11':[f'A make up manufacturer has fixed costs of {p11_fixedcost}, and sells {p11_units} yearly, what is the fixed cost per unit?', round(p11_fixedcost/p11_units)], 
'P12':[f'A software company sells products in Spain, Italy, and the US. The Spanish market has revenues of {p12_rev}, and Italy has {p12_percentageincr} higher sales than Spain. What is the combined total of their revenues?', round(p12_solution)], 
'P13':[f'What is the average productivity in a company with {p13_employees} employees and {p13_output} units of output in a given day? Answer in units produced per employee, please', round(p13_output/p13_employees)], 
'P14':[f'If the COGS is {p14_perc} of a companys revenue, and they made {p14_sales} in sales this year, what is their COGS in dollar amount?' ,  round((p14_perc/100)*p14_sales)], 
'P15':[f'For our new product, we are expecting to spend {p15_invest} in development, and each unit will cost {p15_cost} to produce, while it will be sold for {p15_price}. How many units do we need to sell to breakeven?', round(p15_invest/(p15_price-p15_cost))], 
'P16':[f'Our client has a current revenue of {p16_currentrev} annually, and is expecting to see growth at {p16_y1growth}% in the next year, and a growth of {p16_y2growth} % and {p16_y3growth} % in the following years respectively. What is the expected revenue in year 3? Please round to the nearest integer', round(p16_solution)], 
'P17':[f'Company A currently has a revenue of {p17_rev}, and a profit margin of {p17_profitmargin}. If their expenses are expected to go down by {p17_costreductionperc} % in the next year, what would be their actual costs in dollar amount in that year? Please round to the nearest integer.', round(p17_solution)],
'P18':[f'A technology startup launched a website on Monday. The number of visitors tripled every day until Friday. If the website had {p18_monday_visitors} visitors on Monday, how many visitors did it have on Friday? (Round to nearest Integer)', round(p18_answer)],
'P19':[f'Due to the recent health crisis, George was laid off and was forced to take temporary jobs. He worked {p19_number_hours_worked_week1} hours this week as a cashier at a local supermarket and made ${p19_money_made_week1}. If he works {p19_number_hours_worked_week2} hours next week at the same pay rate, how much money will he make? (Round to nearest integer)', round(p19_answer)],
'P20':[f'You have developed a fitness coaching website that helps people lose weight. It cost you ${p20_domain_name_cost} to buy the domain name from its previous owner, ${p20_it_cost} to hire IT people to develop the site, and then you spent ${p20_marketing_cost} to market the website to law school students. Customers pay ${p20_price} for a lifetime access to your site. How many individual customers do you need to breakeven? (Round to nearest integer)', round(p20_answer)],
} 

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