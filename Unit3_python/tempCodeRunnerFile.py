def foodExpiration(month, date, year):
    expirationMonth: 12 
    expirationDate: 5
    expirationYear: 2026
    if date > expirationDate and year > expirationYear:
        print('throw food away.')
    else:
        print('food is still good.')

foodExpiration(12, 4, 2024)