numbers = [10, 20, 15, 20, 10]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)