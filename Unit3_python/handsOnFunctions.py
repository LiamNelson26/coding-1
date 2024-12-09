# Discuss the anatomy of a function

# a function definition tells the computer
# the instructions on what we want to do with data

# data = just means data types

# curly brackets = passing in data into
# the function definition. This is formally 
# called a parameter

# parameter = placeholder for data

def modifyMyName():
    print('your new modified name is the great '+ name)

# when we pass data into a function call it is called an 
# argument
# argument = evidence, facts, real data.
# modifyMyName('Ian')

# Lesson on Conditional Statements


# Lesson on Conditional Statements 

# conditional statemetns use the 'IF' and 'ELSE' 
# keyword to filter and create specific outcomes
# based on data

def verifyAge(age):
    if age > 17:
        print('Congrats you can buy GTA VI')
    else:
        print('Sorry, you need an adult to but this game.')

verifyAge(19)



# Conditional Statements
# if /else keywords; gives us the ability to
# control outcomes and make decisions on data

# food expiration software is an example of 
# using conditional statements. If the food expires
# it neefs to be thrown away, otherwise, or else
# it can be eaten

def foodExpiration(month, date, year):
    expirationMonth: 12 
    expirationDate: 5
    expirationYear: 2026
    if date > expirationDate and year > expirationYear:
        print('throw food away.')
    else:
        print('food is still good.')

foodExpiration(12, 4, 2024)




