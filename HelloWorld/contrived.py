numbers = [1, 45, 31, 12, 60]
# numbers = [1, 45, 31, 16, 60]

for number in numbers:
    if number % 8 == 0:
        # Reject List
        print("The numbers are unacceptable")
        break
else:
    print("All those numbers are grand")