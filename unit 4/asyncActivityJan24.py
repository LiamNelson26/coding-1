numberList = [1, 23, 56, 3, 56, 3, 20, 200]
numberList.reverse
print(numberList)


def passwordLoops():
    correctPassword1 = 'Amazon26'
    correctPassword2 = '26Amazon'
    userPassword1 = ''
    userPassword2 = ''
    while userPassword1 != correctPassword1:
        print('This password is incorrect. Try Again ')
        userPassword1 = input('Please enter your correct password:')
    while userPassword2 != correctPassword2:
        print('This password is incorrect. Try Again ')
        userPassword2 = input('Please enter your correct password:')

    # if userPw == correctPw:
    else:
        print('congrats')
        print('Correct, you may enter the site')

passwordLoops()
