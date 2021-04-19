import random

# answer = 5
answer = random.randint(1, 10)
highest = 100
print(answer) # TODO, Remove after testing
guess = 0

print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry, you have not guessed correctly")








# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done! You guessed it!")
#     else:
#         print("Sorry!, you have not guessed properly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done! You guessed it!")
#     else:
#         print("Sorry!, you have not guessed properly")
# else:
#     print("You got it first time")

print()

tree1 = 'Oak'
tree2 = 'Silver Birch'

if tree1 == tree2:
    print("The trees are the same")
else:
    print("The trees are different")

print()

x = 5
y = 7

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is smaller than y")
else:
    print("x equals y")


