for index, character in enumerate("abcdefgh"):
    print(index, character)

print()

for t in enumerate("abcdefgh"):
    index, character = t
    # print(t)
    print(index, character)

print()

index, character = (0, 'a')
print(index)
print(character)