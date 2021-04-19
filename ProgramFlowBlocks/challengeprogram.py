input("Hi, welcome to the list of stuff to do in this program."
      " Press ENTER to begin! ")
print("Please select one of the following choices: ")

choice_chosen = "-"
while choice_chosen != "0":
    if choice_chosen in "12345":
        print("\nYou chose {}".format(choice_chosen))
    else:
        print("\nPlease select one of the following choices: ")

        print("1:\tGo shopping")
        print("2:\tGo for a walk")
        print("3:\tGo swimming")
        print("4:\tGo to your friend's house")
        print("5:\tGo to the park")
        print("0:\tExit")

    choice_chosen = input()
