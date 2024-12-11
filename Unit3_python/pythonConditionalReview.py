# functions are just instructions
# for the computer to know what to do
# with data.

# conditional statements use the if/ else
# keywords to make decisions and outcomes 
# based on data.

def welcomeMsgByTime(number,time):
    if time == 'am':
        print('good morning')
        print(str(number)+time)
    elif time == 'pm':
        print('good evening')
        print(str(number)+time)
    elif number > 12:
        print('sorry number cant be greater than 12')
    else:
        print('sorry, did not understand your input')

welcomeMsgByTime(15,'pm')



def numericalGrade(grade,letter):
    if grade == 90:
        print('Congradulations, you have an A+')
        print(str(letter)+grade)
    elif grade == '82':
        print('Congraduations, you have a B-')
        print(str(letter)+grade)
    