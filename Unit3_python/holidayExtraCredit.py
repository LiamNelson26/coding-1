from datetime import date
from multiprocessing import Event


def holidaySchedule(date, event):
    if date == '12/21/24':
        print('Christmas Party')
        print(str(date)+event)
    elif date == '12/22/24':
        print('There is no event planned for that day')
        print(str(date)+event)
    elif date == '12/25/24':
        print('Christmas Day')
    elif date == '12/27/25'
        print('There is no event planned for that day')
        print(str(date)+event)
    elif date == '1/1/25'
        print('There is no event planned for that day.')
        print(str(date)+event)
    else: 
        print('Celebrating New Years Eve')


holidaySchedule(date, Event)
