# for i in range(10):
#     print("i is now {}".format(i))

i = 0

while i < 10:
    print("i is now {}".format(i))
    i += 1


print()

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

print()

for i in range(0, 21):
    if i % 3 != 0 and i % 5 != 0:
        print(i)

print()

# Using Continue
for i in range(0, 21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
