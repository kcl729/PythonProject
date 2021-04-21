import random

#Problem 1 Data
p1_net_income_year1 = random.randrange(100,500,50)                                      
p1_revenue_year1 = random.randrange(500,1000,50)
p1_revenue_year2 = 10  
p1_solution = round(((p1_net_income_year1/p1_revenue_year1)*p1_revenue_year2*1000000000),0)

#Problem 2 Data
p2_number_of_employees = random.randrange(20000,60000,1000)                                      
p2_number_of_partners = random.randrange(200,600,50) 
p2_solution = round((p2_number_of_partners/p2_number_of_employees)*100,0)

#Problem 3 Data
p3_percent_buyers = random.randrange(60,100,5)
p3_percent_sneaker_buyers = random.randrange(10,50,5)
p3_solution = round(100*(p3_percent_buyers/100)*(p3_percent_sneaker_buyers/100),0)

#Problem 4 Data
p4_single_bag_price = random.randrange(1,3,1)
p4_tenpack_bag_price = random.randrange(5,10,1)
p4_solution = round(((1-((p4_tenpack_bag_price/10)/p4_single_bag_price))*100),0)

#Problem 5 Data
p5_number_large_desks = random.randrange(50,100,1)
p5_number_small_desks = random.randrange(1,50,1)
p5_solution = round(((p5_number_small_desks/(p5_number_small_desks + 3*p5_number_large_desks))*100),0)

#Problem 6 Data
p6_number_burguers_sold_2019 = random.randrange(2_000_000,5_000_000,1000)
p6_percentage_increase = random.randrange(10,100,10)
p6_solution = round((p6_number_burguers_sold_2019/(1+p6_percentage_increase/100)),0)

#Problem 7 Data
p7_initial_price = random.randrange(50,100,5) 
p7_percentage_increase = random.randrange(2,10,1)
p7_discount = random.randrange(10,30,1)
p7_solution = round((p7_initial_price*(1+(p7_percentage_increase/100))*(1-(p7_discount/100))),0)

#Problem 8 Data
p8_investment = random.randrange(100000,300000,100000)
p8_rev = random.randrange(290, 505, 30)
p8_cost = random.randrange(100,200, 50)
p8_solution = round((p8_investment/(p8_rev-p8_cost)),0)

#Problem 9 Data
p9_investment = random.randrange(500000,15000000, 500000)
p9_growthrate = random.randrange(20,40,10)
p9_periods = random.randrange(2,4,1)
p = 0 
p9_endamount = p9_investment 
while p < p9_periods:
    p9_endamount = p9_endamount * p9_growthrate
    p += 1
#check with Amber

#problem 10 data
p10_percentage = random.randrange(13,21,3)
p10_quantity = random.randrange(800000, 950000, 50000)
p10_solution = round(((p10_percentage/100)*p10_quantity),0)

# problem 11 data
p11_fixedcost = random.randrange(3000000, 4000000, 500000)
p11_units = random.randrange(175000, 225000, 25000)
p11_solution = round((p11_fixedcost/p11_units),0)

# problem 12 data 
p12_rev = random.randrange(250000, 350000, 50000)
p12_percentageincr = random.randrange(22,32,5)
p12_solution = round((p12_rev + (1+(p12_percentageincr/100))*p12_rev),0)

# problem 13 data
p13_output = random.randrange(120000,170000,25000)
p13_employees = random.randrange(55,75,10)
p13_solution = round((p13_output/p13_employees),0)

# problem 14
p14_perc = random.randrange(10,14,2)
p14_sales = random.randrange(130000000,150000000,20000000)
p14_solution = round(((p14_perc/100)*p14_sales),0)

# problem 15
p15_invest = random.randrange(850000,1050000,20000)
p15_cost = random.randrange(100,200,50)
p15_price = random.randrange(250,400,50)
p15_solution = round((p15_invest/(p15_price-p15_cost)),0)

# problem 16
p16_currentrev = random.randrange(1000000,2000000,500000)
p16_y1growth = random.randrange(3,5,1)
p16_y2growth = random.randrange(5,7,1)
p16_y3growth = random.randrange(2,5,1)
p16_y1rev = p16_currentrev * (1+p16_y1growth/100)
p16_y2rev = p16_y1rev * (1+p16_y2growth/100)
p16_solution = round((p16_y2rev * (1+p16_y3growth/100)),0)

# problem 17
p17_rev = random.randrange(1000000,2000000,500000)
p17_profitmargin = random.randrange(9,13,2)
p17_costreductionperc = random.randrange(10,30,10)
p17_costs = (100-p17_profitmargin)/100*p17_rev
p17_solution = round((p17_costs * ((100-p17_costreductionperc)/100)),0)

#Problem 18
p18_monday_visitors = random.randrange(100,1000,50)
p18_solution = round((p18_monday_visitors*3**4),0)

#Problem 19
p19_number_hours_worked_week1 = random.randrange(15,40,1)
p19_money_made_week1 = random.randrange(110,150,1)
p19_number_hours_worked_week2 = random.randrange(10,45,1)
p19_solution = round(((p19_money_made_week1/p19_number_hours_worked_week1)*p19_number_hours_worked_week2),0)

#Problem 20
p20_domain_name_cost = random.randrange(900,3000,50)
p20_it_cost = random.randrange(12000,30000,100)
p20_marketing_cost = random.randrange(7000,20000,100)
p20_price = random.randrange(50,150,5)
p20_solution = round(((p20_domain_name_cost+p20_it_cost+p20_marketing_cost)/p20_price),0)

# problem 21
p21_big_num = random.randrange(200, 400, 20)
p21_students = random.randrange(30, 70, 5)
p21_alumni = random.randrange(20, 80, 5)
p21_solution = round((p21_big_num*p21_students/100*p21_alumni/100),0)

# problem 22
p22_big_price = random.randrange(20000000, 100000000, 10000000)
p22_percent = random.randrange(10, 40, 5)
p22_solution = round((p22_big_price*(1-p22_percent)),0)

# problem 23
p23_crew_1 = random.randrange(30, 70, 10)
p23_crew_2 = random.randrange(40, 80, 10)
p23_solution = round((1/(1/p23_crew_1 + 1/p23_crew_2)),0)

# problem 24
p24_quiz_per = random.randrange(10, 25, 5)
p24_par_per = random.randrange(20, 40, 5)
p24_exam_per = 100-p24_quiz_per-p24_par_per
p24_par_grade = random.randrange(80, 100, 2)
p24_quiz_grade = random.randrange(70, 100, 5)
p24_exam_grade = random.randrange(70, 100, 5)
p24_solution = round((p24_exam_per/100*p24_exam_grade+p24_par_grade*p24_par_per/100+p24_quiz_per/100*p24_quiz_grade),0)

# problem 25
p25_last_month = random.randrange(8, 10, 1)
p25_this_month = random.randrange(12, 18, 2)
p25_solution = round((((p25_this_month-p25_last_month)/p25_last_month)*100),0)

# problem 26
p26_ducky_buy = random.randrange(400, 800, 100)
p26_ducky_sell = random.randrange(1, 4, 1)
p26_solution = round(((p26_ducky_sell-(p26_ducky_buy/1000))/p26_ducky_buy),0)

# problem 27
p27_start_month = random.randrange(10000, 30000, 2000)
p27_end_month = random.randrange(60000, 90000, 5000)
p27_solution = round((p27_end_month/p27_start_month*100-100),0)

# problem 28
p28_cost_marketing = random.randrange(5000, 25000, 10000)
p28_cost_app_dev = random.randrange(15000, 55000, 10000)
p28_cost_class_dev = random.randrange(10000, 40000, 10000)
p28_lifetime_membership = random.randrange(20, 100, 10)
p28_solution = round(((p28_cost_app_dev+p28_cost_class_dev+p28_cost_marketing)/p28_lifetime_membership),0)

# problem 29
p29_base_pay = random.randrange(10000000, 50000000, 5000000)
p29_percent_earnings = random.randrange(4, 40, 5)
p29_solution = round((100/p29_percent_earnings*p29_base_pay),0)

# problem 30
p30_gamestop_price = random.randrange(3, 10, 1)
p30_gamestop_growth = random.randrange(600, 1400, 20)
p30_outstanding_shares = random.randrange(60, 80, 2)
p30_solution = round(((p30_gamestop_price*p30_gamestop_growth-p30_gamestop_price)*p30_outstanding_shares),0)

#problem dictionary
problem_dictionary = {
'P1':[f'Facebook had net income of ${p1_net_income_year1:,} million in 2009 on revenue of ${p1_revenue_year1:,} million. Figures for 2010 weren\'t disclosed yet, but analysts have said the company\'s revenue in 2010 could be as much as ${p1_revenue_year2:,} billion, fueled by advertising growth. If Facebook maintained the same profit margin as in 2009, what would be their net income in 2010? Please round your answer to the nearest integer',p1_solution],
'P2':[f'About {p2_number_of_partners:,} of Goldman Sachs (NYSE:GS)\'s roughly {p2_number_of_employees:,} employees have the title of partner, what\'s the percentage of partners among all Goldman Sachs employees? Please round your answer to the nearest integer',p2_solution],
'P3':[f' The manager of an clothing store in Boston needed to calculate the percentage of customers who purchase sneakers. Upon completing her survey, she noticed that {p3_percent_buyers:,}% of the people that entered her store purchased an item. Of those customers, {p3_percent_sneaker_buyers:,}% percent purchased sneakers. What percent of the people that entered the clothing store purchased sneakers? Please round your answer to the nearest integer',p3_solution],
'P4':[f'The price of a bag of chips is ${p4_single_bag_price:,}. The price of a ten pack of the same bag of chips is ${p4_tenpack_bag_price:,}. The ten pack of bag chips is what percentage cheaper than purchasing ten bag of chips individually? Please round your answer to the nearest integer',p4_solution],
'P5':[f'An office manager purchased {p5_number_large_desks:,} large desks and {p5_number_small_desks:,} small desks. If the price of a large desk is three times the price of a small desk, what percent of the total cost was the cost of the small desks? Please round your answer to the nearest integer', p5_solution],
'P6':[f'The number of plant-based burguers sold in Boston during 2019 was {p6_number_burguers_sold_2019:,}; up {p6_percentage_increase:,}% from three years before. How many burguers were sold three years before 2019?',p6_solution], 
'P7':[f'A chair in Wayfair\'s webiste was priced at ${p7_initial_price:,}. The marketing manager thought he could get more money for the chair, so he increased its price by {p7_percentage_increase:,}%. After a week, the chair had not been sold. The manager then discounted the new price by {p7_discount:,}%, and the chair was finally sold. For how much was the chair sold? Please round your answer to the nearest integer',p7_solution], 
'P8':[f'What is the breakeven quantity for a business that required an initial investment of ${p8_investment:,}, where each unit brings in ${p8_rev:,} of revenue but each unit costs ${p8_cost:,}?', p8_solution], 
'P9':[f'What is the expected NPV for an investment of ${p9_investment:,}, where the annual growth rate is expected to be {p9_growthrate:,}% after {p9_periods:,} periods?', round(p9_endamount)], 
'P10':[f'What is the addressable market size (in units) for company A if they want to reach {p10_percentage:,}% of a total of {p10_quantity:,} units? Please round your answer to the nearest integer', p10_solution], 
'P11':[f'A make-up manufacturer has fixed costs of ${p11_fixedcost:,}, and sells {p11_units:,} units yearly. What is the fixed cost per unit? Please round to the nearest integer', p11_solution], 
'P12':[f'A software company sells products in Spain, Italy, and the US. The Spanish market has revenues of ${p12_rev:,}, and Italy has {p12_percentageincr:,}% higher sales than Spain. What is the combined total of their Spain and Italy revenues? Please round your answer to the nearest integer' , p12_solution], 
'P13':[f'What is the average productivity in a company with {p13_employees:,} employees and {p13_output:,} units of output in a given day? Please answer in units produced per employee rounded to the nearest integer', p13_solution], 
'P14':[f'If COGS are {p14_perc:,}% of a company\'s revenue, and they made ${p14_sales:,} in sales this year, what is their COGS in dollar amount for this year? Please round your answer to the nearest integer' , p14_solution], 
'P15':[f'For our new product, we are expecting to spend ${p15_invest:,} in development, and each unit will cost ${p15_cost:,} to produce, while it will be sold for ${p15_price:,}. How many units do we need to sell to breakeven?', p15_solution], 
'P16':[f'Our client has a current revenue of ${p16_currentrev:,} annually, and is expecting to see growth at {p16_y1growth:,}% in the next year, and a growth of {p16_y2growth:,}% and {p16_y3growth:,}% in the following years respectively. What is the expected revenue in year 3? Please round to the nearest integer', p16_solution], 
'P17':[f'Company A currently has a revenue of ${p17_rev:,}, and a profit margin of {p17_profitmargin:,}%. If their expenses are expected to go down by {p17_costreductionperc:,}% in the next year, what would be their actual costs in dollar amount in that year? Please round to the nearest integer.', p17_solution],
'P18':[f'A technology startup launched a website on Monday. The number of visitors tripled every day until Friday. If the website had {p18_monday_visitors:,} visitors on Monday, how many visitors did it have on Friday? Please round your answer to the nearest integer', p18_solution],
'P19':[f'Due to the recent health crisis, George was laid off and was forced to take temporary jobs. He worked {p19_number_hours_worked_week1:,} hours this week as a cashier at a local supermarket and made ${p19_money_made_week1:,}. If he works {p19_number_hours_worked_week2:,} hours next week at the same pay rate, how much money will he make? Please round your answer to the nearest integer', p19_solution],
'P20':[f'You have developed a fitness coaching website that helps people lose weight. It cost you ${p20_domain_name_cost:,} to buy the domain name from its previous owner, ${p20_it_cost:,} to hire IT people to develop the site, and then you spent ${p20_marketing_cost:,} to market the website to college students. Customers pay ${p20_price:,} for a lifetime access to your site. How many individual customers do you need to breakeven? Please round your answer to the nearest integer', p20_solution],
'P21':[f'At a recent networking event held by Babson College with {p21_big_num:,} attendees, {p21_students:,}% of the people present were at one point Babson students, and {p21_alumni:,}% of these students are currently enrolled at Babson. What percent of people present were current students? Please round your answer to the nearest integer', p21_solution],
'P22':[f'In 2019 Macys built a new headquarters in boston for ${p22_big_price:,}, but after the outbreak of Coronavirus, they decided to sell the headquarters at a {p22_percent:,}% loss. How much did they sell the headquarters for? Please round your answer to the nearest integer', p22_solution],
'P23':[f'Seaside Construction has two project crews. Crew 1 can complete a house in {p23_crew_1:,} days on average, while it takes crew 2 {p23_crew_2:,} days. How long would it take them to finish an average house working together? Please round your answer to the nearest integer', p23_solution],
'P24':[f'In Babson\'s most popular class, Techonolgy and Operations Management, participation is worth {p24_par_per:,}% of the grade, quizzes are worth {p24_quiz_per:,}% of the grade, and exams make up the remaining percent. What final grade would someone with a {p24_par_grade:,} in participation, {p24_quiz_grade:,} in quizzes, and {p24_exam_grade:,} on exams have? Please round your answer to the nearest integer', p24_solution],
'P25':[f'Dunder Mifflin\'s paper sales staff acquired {p25_last_month:,} new clients last month. This month a sale was offered for new customers and they acquired {p25_this_month:,} new clients. What was their percent increase in sales? Please round to the nearest integer',p25_solution ],
'P26':[f'Ducky Import/Export Company purchases rubber ducks from their supplier in China for ${p26_ducky_buy:,} per thousand. They then resell them in the United States for ${p26_ducky_sell:,} each. What is the percent markup on each rubber duck? Please round your answer to the nearest integer', p26_solution],
'P27':[f'Over the past month Bitcoin has climbed from a price of ${p27_start_month:,} at the start of the month to a high of ${p27_end_month:,} today. If you bought at the start of the month, what percent return would you have obtained?', p27_solution],
'P28':[f'You have decided to develop an app that teaches people how to code. The cost of hiring programmers to code the app is ${p28_cost_app_dev:,}, the cost of marketing is ${p28_cost_marketing:,}, and the cost of developing the classes is ${p28_cost_class_dev:,}. You sell a lifetime membership for ${p28_lifetime_membership:,}. How many memberships do you need to sell to breakeven? Please round your answer to the nearest integer', p28_solution],
'P29':[f'Tim Cook, the CEO of Apple, brought home ${p29_base_pay:,} in base pay last year. Taking into account bonuses, stock options, and other benefits his base pay was {p29_percent_earnings:,}% of his total earnings. How much did Tim Cook earn last year?', p29_solution],
'P30':[f'This year the share price of Gamestop has risen by {p30_gamestop_growth:,}% from its start of year price of ${p30_gamestop_price:,} per share. Gamestop currently has {p30_outstanding_shares:,} outstanding shares. By what amount (in dollars) has its market capitalization grown in this period? Please round your answer to the nearest integer', p30_solution]
}