# Declaring the dictionary
countries = {}

# User enters the length ogf the dictionary
num = int(input("Enter how many countries do you want to enter: "))

for i in range(num):
    key = input("Enter the country: ")
    value = input("Enter the capital: ")
    countries[key] = value

for key, value in countries.items():
    print(key, '-', value)