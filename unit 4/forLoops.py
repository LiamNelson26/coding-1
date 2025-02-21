groceryList = ['apple', 'water', 'milk,''chicken']

# FOR LOOPS - Is a type of loop that iterate over a list.
# It will go through your list and do whatever operation
# you want it to do.

# for loops use an iterator, which is just a variable
# this is intended to represent a value in the list.

# then "IN" keyword gives us access to the list we
# want to go through

groceryList = ['apple', 'water', 'milk', 'chicken']
for x in groceryList:
    if x == 'milk':
        # groceryList.remove(x)
        continue
    print(x)


gradeList = [100, 70, 90, 70, 65, 95]

for grade in gradeList:
    if grade < 75:
        continue
    print(grade)

for grade in gradeList:
    gradeList.append(85)
    print(grade)
    break

#  add all the number together and then return the
#  value in the for loop.
