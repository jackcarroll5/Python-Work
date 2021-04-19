print("Today is a grand day to learn Python")
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
print("Hello" + " world")
print()

greeting = "Hello" #Uppercase and lowercase variables = Different Values
#name = input("Please enter your name ")
name = "Jack"
print(greeting + name)
print(greeting + ' ' + name)

age = 24
print(age)
print()

print(type(greeting))
print(type(age))
print()

ageInWords = "2 years" #Example why Python particular in language
print(ageInWords)
#print(name + " is " + age + " years old")
print(name + f" is {age} years old")
print(age)
print(type(age))
print(type(ageInWords))
print()

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")