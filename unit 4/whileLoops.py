import random

# Loops - A construct in programming
# where instructions will repeat over and 
# over until a specific condition is met. 

# While loop - is a special type of loop where
# instructions will repeat themselves
# so long as a condition is true.

def repeatMs():
    x = 2
while x == 2:
    print('this message will repeat forever. ')

def passwordLoops():
    correctPw= '123abc'
    userPw=''
    while userPw != correctPw:
        print('incorrect pw. Try Again ')
        userPw=input('please enter your password:')
    # if userPw == correctPw: 
    else:
        print('congrats')
        break:
        print('Correct, you may enter the site')
passwordLoops()

# passwordLoops()
 
def inventoryLoop():
    userInventory =[] 
    pickupItem= input('what item are you picking up?: ')
    while len(userInventory) == 0:
        userInventory.append(pickupItem)
        print('these are the items in your bag: ')
        print(userInventory)
        pickupItem= input('what item are you picking up?: ')

# inventoryLoop()

# def replaceInventoryItem() save for another day
# def removeInventoryItem() save for another day

def rngGame():
    randomNumber = random.randrange(1,11)
    print(randomNumber)
    userAnswer =''
    while randomNumber != userAnswer:
        UserInputGuess = int(input("Guess a number between 1 and 10: "))
        userAnswer= UserInputGuess
        print('incorrect guess. Try again')
    else:
        print('this is the correct answer. ')

rngGame()



def passwordCheck():
    correctPassword: 12659391
    userPassword = ''
    while userPassword != correctPassword
        print('This password is incorrect password. Please try again. ')
    else:
        print('This passwoard is correct, you may continue.')

passwordCheck()
    