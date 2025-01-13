# Create a function that will determine what
# level of education a college student is in.
# based on the number of years they've been in
# school

# undegrad 1 freshman, 2 sophmore, etc...
# 5 masters degree, doctorate degree, etc...

collegeTitles= ['freshman', 'sophmore', 'junior', 'senior']
print(len(collegeTitles))


def gradeToTitle():
    # input is a buildt-in function that lets us pass data into our
    # program AS STRINGS.

    # int() is also a built in function that transforms anything inside 
    # of its round brackets into an integer number.
    # the first 3 letters of integer are INT.

    year = int(input('What year are you in?'))
    if year == 1:
        print('you are a freshman in undergrad')
    elif year == 2:
        print('you are a sophmore in undergrad.')
    elif year == 3:
        print('you are a junior in undergrad.')
    elif year == 4:
        print('you are a senior in undergrad.')
    elif year == 5 or year == 6:
        print('you are in a masters program and in grad school.')
    elif year >= 7 and year <= 10:
        print('you are in a doctorates program and in grad school')
    elif year > 11:
        print('you need to go get a job, you have been in school too long.')
    else:
        print('Err: something went, please check you in')




gradeToTitle(year)

# A laist is a data type for collecting
# and organizing other data types.

# we create a list by giving it a variable name and using
# the square brackt to place the data inside of

listB = [10, 102, 4984]

listOfData = ('words and characters',
              10,
              10.2324,
              True,
              False,
              listB
              )
print(listOfData)

collegeTitles = ('freshman', 'sophmore', 'junior', 'senior')

print(collegeTitles[0])