numbers = input("Please enter three numbers: ")
numbered_list = numbers.split(",")

for i in range(len(numbered_list)):
    numbered_list[i] = int(numbered_list[i])

solution = numbered_list[0] + numbered_list[1] - numbered_list[2]
print(solution)