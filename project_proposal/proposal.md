**1\. The Big Idea**

A large portion of Americans have challenges tracking and paying their expenses. According to a 2018 survey of 1,500 people, "65 percent of Americans said they don't know how much they spent last month" (Intuit Mint Life). The same survey also showed that "nearly a third of Americans wish they'd spent less in the last month". These financial challenges are caused by several factors. One of these factors seems to be a lack of habits in expense tracking, as shown by a study from the National Foundation for Credit Counseling, which found that "61% of US adults don't keep track of their money".

To address the need of consumers to track their expenses, we propose building an easy-to-use personal expense tracker. The expense tracker will be a web app where users can input their daily expenses to store the information in one place. Each expense will have a $ amount, a category, a sub-category, and additional comments. Over time, the platform can use the information imputed by the user to provide visualizations with weekly insights and trends about spending habits. Ultimately, users will be able to leverage these insights to manage and even reduce expenses over time.

To effectively build this solution, we will explore topics in both personal finance and software design. In personal finance, we will need to research the different and mutually exclusive categories and subcategories in which expenses can fit in. For instance, for the platform to be able to categorize a Netflix subscription expense, it must be programmed to classify this expense into the corresponding category. In software design, we will need to explore the design of large and complex functions. Potentially, we may need to also explore how to use APIs, such as Plaid, in Python.

The minimum viable product for this project is best described as a combination of two functions in Python and graphs in MS Excel. The first function, called expense_categorizer(), will ask the user to input an expense with its $ amount and will return the category and subcategory of the expense. The second function, called expense_tracker(), can store the information imputed through the expense_categorizer function in a table. After a week of users testing the solution by inputting their expenses into the functions, we can export the data in the table and use it to create graphs such as bar charts for the user. This experiment would be a resource-efficient way of testing whether users benefit from storing their expense information and learning insights about them.

If our solution exceeds our expectations, a stretch goal could be to find a way to integrate the expense tracker with users' bank accounts so that the expenses are automatically inputted into the platform rather than having the user input them themselves, by using the Plaid API to pull information directly from people's bank accounts. Plaid offers a seamless user experience for logging into a variety of major banks' applications and accessing personal expenses. Since our goal is to empower anyone who is looking to improve their financial health, we will consider building both versions so that we can reach a wider audience. 

**2\. Learning Goals**

Through this project, our group would like to learn how to:

-   Design a software solution in response to a specific user need

-   Design a software solution that is mutually exclusive and collectively exhaustive in terms of the possible inputs that it can receive from users

-   Build a web application based on a python program

-   Combine data analysis and programming to become more comfortable with larger sets of data

-   Integrate an API with a Python program

-   Build agile, flexible visualizations that deliver value from what we have built on the back end, to the app users 

-   We intend to create a finalized product that shows our mastery of python, so that we can put it in our personal portfolios.

3\. Implementation Plan: this will probably be pretty vague initially. Perhaps at this early juncture you will have identified a library or a framework that you think will be useful for your project. If you don't have any idea how you will implement your project, provide a rough plan for how you will determine this information.

-   Explore Plaid integration and possible applications for the API

-   Sketch, improve, and program the front-end of the application 

-   Create and test the user interface for our application

-   Build out the concept of the program more: what should users have access to? What information should be presented to them

-   Interview potential users about what functionality they want in the expense tracker

**4\. Project schedule**
|

Date

 |

Goal to Complete

 |
|

3/05

 |

Each group member should have looked through and tested the  Plaid API.

 |
|

3/19

 |

All pseudocode should be completed

 |
|

4/02

 |

The basic user interface, user inputs, and expense tracking functionality should be complete

 |
|

4/09

 |

User interface remastered/finalized, any expense predicting/recommending completed, test run with group of friends should be started.

 |
|

4/14

 |

Final testing and editing - code should be complete by this point

 |

**5\. Collaboration plan: **

Since we have a broad variety of skill sets, we will mostly aim to divvy up the workload and hold frequent check-ins to share our progress, do code reviews, work out blockers, and brainstorm the direction of our project. We can aim to check-in on Mondays and Thursdays, concurrently giving each team member the opportunity to self-manage tasks. 

One of our focuses will be on communicating, over slack, what we are working on so that we can finish the project as efficiently as possible. In this way we hope to minimize the amount of overlapping work group members do so that we have time to complete more of the project. 

We have an agile based project timeline setup. The check ins will be bi-weekly at the beginning of the semester, with more check-ins happening near the due date because we will have better knowledge of Python then (and should be able to code faster/better) and it will be more important to touch base and ensure the interconnectivity of all parts of the application. For this reason, the goals are relatively broad, especially near the end of the semester since we don't have perfect knowledge of what the application will look like by that point in development. We felt that this was the best method of planning work since we are still learning Python, and what we learn during the semester may dramatically change the scope of the project.

**6\. Risks:** 

1.  (Lack of) focus: The project entails more than writing a Python script and developing an application. It has elements of front-end development and product management, so we want to make sure the bulk of our work contributes to our skill building of Python and the project expectations. In order to mitigate this, we should design a very simple but nice-looking UI and take advantage of Plaid's uses. 

2.  Time: our expense tracker has a lot of potential, so we should be wary of scope creep. We should stick to building out the basics well, and be mindful of evaluating other application features against how useful they are/how much time they would take to be added on/how much pursuing them would add to our knowledge and skills base

3.  Communication: When working with multiple people on a coding project it is easy to work on overlapping functions and processes without good communication, so by keeping each other updated on our work we can be more time efficient.

**7\. Additional Course Content:** 

A class where we work on integrating python with Excel/SQL through the use of APIs would be useful for helping us complete the expense tracker. Additionally, a 10-20 minute segment on best practices for information storage and analysis (to minimize data used) would be helpful for both this project and future career prospects.

Works Cited:

<https://mint.intuit.com/blog/budgeting/spending-knowledge-survey/>

https://www.businessinsider.com/personal-finance/61-of-us-adults-dont-keep-track-of-their-money-2014-4
