activity = input("What would you like to do today? ")

#casefold = Turns string to lowercase but handles different character sets better
if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")