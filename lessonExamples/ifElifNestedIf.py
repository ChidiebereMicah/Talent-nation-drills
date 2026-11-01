#THE IF STATEMENT
#Primarily used when you want to perform an action based on a given condition
#The way an if statement is structured:
# if condition:
#     do action

#Example
# car_dealer = 'mercedes'
# if car_dealer == 'mercedes':
#     print('Buy car')

#====================================================

#THE IF ELSE STATEMENT
#Primarily used when you you want to perform an action based on a given condition but perform another action if that initial condition was not met
#The if-else statement is structured this way:
# if condition:
#     do action
# else:
#     do a different action
#Example

# account_bal = 100000
# if account_bal > 100000:
#     print('Buy mercedes')
# else:
#     print('Buy bicycle')

#====================================================

#THE IF ELIF STATEMENT
#Just like the if else but it is used when considering several conditions in a given order of priority. The action is performed for the first condition that is satisfied and the if elif block is exited.
# if condition_1:
#     do action_1
# elif condition_2:
#     do action_2
# elif condition_3:
#     do action_3
#     .
#     .
#     .
# else:
#     do default_action

#The last else is added if there is a default action you want to do when all the conditions are not met.
# Example:
# available_cars = ['mercedes', 'lamborgini', 'aston martin', 'porsche', 'toyota']
# if 'lamborgini' in available_cars:
#     print('buy lamborgini')
# elif 'aston martin' in available_cars:
#     print('buy aston martin')
# elif 'porsche' in available_cars:
#     print('buy porsche')
# elif 'mercedes' in available_cars:
#     print('buy mercedes')
# elif 'toyota' in available_cars:
#     print('buy toyota')
# else:
#     print('buy keke-napep') #default

# Remove lambo and aston martin from the list of available cars and see what gets printed

#====================================================

#THE NESTED IF STATEMENT
#The nested if is used when you want to check another condition while already performing the action for an initial if statement:
# if condition:
#     if nested_condition:
#        then do action

#You can nest as many times as desired
# if condition:
#     if nested_condition:
#        if nested_nested_condition:
#             then do action

# Example
# car_dealer = 'mercedes'
# car_color = 'dark_brown'
# if car_dealer == 'mercedes':
#     if car_color == 'dark_brown':
#         print('buy mercedes')

#====================================================

#COMBINING THE CONDITIONAL STATEMENT CONCEPTS
# You can combine the if, if else, elif, and nested if blocks in any order depending on the logic you wish to design

# For instance, let's say we want to buy a car but the color would depend on which car we are buying
# available_cars = ['mercedes', 'lamborgini', 'porsche', 'aston martin', 'toyota']
# available_colors = ['red', 'green', 'blue', 'dark brown', 'black']
# if 'lamborgini' in available_cars:
#     if 'red' in available_colors:
#         print('buy red lamborgini')
# elif 'aston martin' in available_cars:
#     if 'green' in available_colors:
#         print('buy green aston martin')
# elif 'porsche' in available_cars:
#     if 'blue' in available_colors:
#         print('buy blue porsche')
# elif 'mercedes' in available_cars:
#     if 'dark brown' in available_colors:
#         print('buy dark brown mercedes')
# elif 'toyota' in available_cars:
#     if 'black' in available_colors:
#         print('buy black toyota')
# else:
#     print('buy yellow keke-napep') #default

#Remove red from available colors and we se that there would be no output because the nested condition in the first if block is not met'

#====================================================

#EXERCISE
#Paste all this code on chatgpt and then include this prompt below

#I just went through this python lesson. Give me 5 exercises that will test my understanding of the concepts explained in the code
