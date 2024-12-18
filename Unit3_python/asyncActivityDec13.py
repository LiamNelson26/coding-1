def integerFunction (positive,number):
    if number == '10':
        print('this is a positive number')
        print(str(positive)+negative)
    elif number == '-12':
        print('this is a negative number')
        print(str(positive)+negative)


def IntegerDetection(x):
    if x > 0:
        print('this is positive.')
    elif x == 0:
        print('this is a zero.')
    else:
        print('this number is negative.')
IntegerDetection(-7)

def movieTicketPriceByAge()


def discountFunction(membership, itemPrice): 
    if membership == 'superShopper':
        print(' you are getting 10 percent off.')
        discount= ItemPrice * .1
        total= itemPrice - discount
        print(total)

    elif membership== 'megaShopper':
        print(' you are getting 15 percent off.')
        discount= ItemPrice * .15
        total= itemPrice - discount
        print(total)
    elif membership== 'ultraShopper':
        print(' you are getting 20 percent off.')
        discount= ItemPrice * .2
        total= itemPrice - discount
        print(total)
    else: 
        print('Error: sorry, that membership  type doesnt exist.')

discountFunction('superShopper', 269)
    