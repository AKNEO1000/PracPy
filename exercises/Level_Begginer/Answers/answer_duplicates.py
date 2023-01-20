# Answer:
numbers = [1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 7, 8, 8, 9, 9, 10]
duplicates = []
for number in numbers:
    if numbers.count(number) > 1:
        duplicates.append(number)
    else:
        continue
print(duplicates)