# Age group categorization

age = int(input("Enter your age: " ))

if age < 13:
    print('child')
elif age < 20:
    print('teenager')
elif age < 60:
    print('adult')
else:
    print('senior')

# Movie ticket pricing

age = int(input("Enter your age: " ))
day = input('Enter which day of the week is this : ')

price = 12 if age >= 18 else 8

if day=='wednesday':
    price -= 2

print('your ticket pricing is : ', price)