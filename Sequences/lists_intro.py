computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

for part in computer_parts:
    print(part)

print(computer_parts)

print(computer_parts[3:])

#Slice replaced by contents of iterable (Each char of slice added - Individually)
# computer_parts[3:] = "trackball"

computer_parts[3:] = ["trackball"] # Items at end replaced by trackball
print(computer_parts)



# computer_parts[3] = "trackball"
# print(computer_parts)

# print()
# print(computer_parts[2])
#
# print()
# print(computer_parts[0:3])
#
# print()
# print(computer_parts[-1])