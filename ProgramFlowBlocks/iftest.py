name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 18 <= age < 31:
    print("Welcome to the holiday, {0}".format(name))
else:
    print("Sorry {0}! You are not at the age range required!".format(name))