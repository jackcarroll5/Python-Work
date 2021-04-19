
parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])
print(parrot[4])
#print()
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[-1])
print(parrot[-14])

print()

print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

print()

print(parrot[0:6]) #Up to but not including last number e.g. 6
print(parrot[-14:-8])
print()

print(parrot[3:5])
print(parrot[-11:-9])
print()

print(parrot[0:9])
print(parrot[:9])
print(parrot[-14:-5])
print()

print(parrot[10:14])
print(parrot[10:])
print(parrot[-4:])
print()

print(parrot[:6])
print(parrot[6:])
print(parrot[-8:])
print()
print()

print(parrot[:6] + parrot[6:])
print(parrot[:])#Starts at beginning and extends to end of sequence
print(parrot[-14:])
print()

print(parrot[-4:-2])
print(parrot[-4:12])

print()

letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[:5] + letters[:7])
print()

print(parrot[0:6:2])
print(parrot[0:6:3])
print()

# number = "9,223;372:036 854,775;807"
# separators = number[1::4]
number = input("Please enter a series of number, using any separators you like: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

# print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))

print()

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

for character in quote:
    if character.isupper():
        print(character)


