# What are loops
# Python Loop is a programming concept where
# code repeats itself under specific conditions. 

# In python, there are 2 versions of loops; for loop and
# while loop.

# While Loops  A type of loop will repeat a 
# set of instructions so long as some condition is true.

hp = 100
normalAttack = 2
specialAttack = 4
increaseHealth = 3

def battleFunction():
    hp = 10
    while hp > 0:
        print('Do you want to attack')
        print(hp)
        hp -= normalAttack
        keepGoing = input('do you want to keep playing ?')
        if keepGoing == 'y':
            print('run function again')
        else:
            print('game over')

# battleFunction()

# For Loops - This is a type of loop that iterates over a collection
# of data and will run a specific set of instructions on data. 

# x in this example, is an iterator. This x represent the numbers
# in the list.

# for every number, we want to simply print it out.

numbers = [1.2.3.4.5.6.7.8]

#for x in numbers: 
    #print(x)

attackValues =[10,25,50, 90]

for attacks in attacksValues:
    print (attacks * 2) 

# Create afunction where item over $50.00 get a 10% discount
def shoppingDiscountFunction():
    shppingCCart = ['demo']
    cartCount = len(shoppingCart)
    print(cartCount)
    while cartCount > 0:
        customerItem = input("how much does this item cost? ")
        shppingCCart.append(shppingCCart)
        print("here are the item price in your cart: ")
        print(shppingCCart)

shoppingDiscountFunction()