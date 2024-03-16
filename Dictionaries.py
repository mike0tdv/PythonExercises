# Declaring the dictionary
countries = {}

# User enters the length ogf the dictionary
num = int(input("Enter how many countries do you want to enter: "))

# Filling the dictionary with contents
for i in range(num):
    key = input("Enter the country: ")
    value = input("Enter the capital: ")
    print()
    countries[key] = value

# Printing out the contents
for key, value in countries.items():
    print(key, '-', value)
print()

# User checks for mistakes
ans = input("Are there any mistakes? (y/n): ")
ans = ans.lower()

while ans == "y":
    print()

    # printing out the keys so the user can specify for which country the entered value is incorrect
    for key in countries.keys():
        print('-', key)
    print()
    key_check = input("For which of the countries: ") # Enters the key of choice

    # Checks to find the key and asks the user to update the value
    for key in countries.keys():
        if key == key_check:
            update = input('Enter the correct capital: ')
            countries[key] = update
    print()

    # Asks if there are any more mistakes
    for key, value in countries.items():
        print(key, '-', value)
    print()
    ans = input("Are there any more mistakes? (y/n): ")
    ans = ans.lower()
else: print("Okay, Bye!")
