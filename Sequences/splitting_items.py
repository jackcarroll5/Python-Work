panagram = """The quick brown 
fox jumps\tover
the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
nos = numbers.split(",")
print(nos)

numbers_new = []

for i in range(len(nos)):
    new_list = nos[int(i)]
    numbers_new.append(int(new_list))

print(numbers_new)

