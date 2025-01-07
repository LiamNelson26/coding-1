# data types - level 1: most basic buildings block
# code, (numbers, letters, true or false)

# operators - level 2: the ability to manipulate and
# do things with data types
# (math, comparisons, assignments, etc)

# functions - level 3: taking the first two concepts and 
# organizing these operations and data tpes
# into instructions

# conditional statement: level 3a: being able
# to add more control on our functions instructions.


# Billing System Function.
# Goal: be able to check and see if a user is past
# due or up-to-date on their subscription

# step 1: we need to have a function definition. 
# this tells the compiuter what our function does 

# user - username=string
# user - userPaymentDate = string/ integer
# user - PaymentAmount= integer

# we need to know if their account is
# passt due OR up-to-date

# function definition - tells the computer what the
# function actually does and how its supposed to work.
def checkSubscription( userDueDate, userMoneyInAccount):
    if userDueDate == 6:
        if userMoneyInAccount == True:

    dueDate = '1/7/2025'
    userPaymentDate  = '1/6/2025'
    moneyInAccount = True
        print('subscription is paid- auto withdraw payment.')
    else: 
        print('payment is not due yet.')
# functinn call - tells the computer tolls the computer to run our instructions

checkSubscription(7. False)

