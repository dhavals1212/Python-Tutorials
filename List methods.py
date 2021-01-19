numbers = [5, 2, 1, 4, 7]

num2 = numbers.copy()
#This will copy the original list to the new list.

numbers.append(20)
#Here 'append' command will add 20 to the very last of the list.

numbers.insert(0,35)
#'insert' method will add number 35 to the 0th index.

numbers.remove(5)
#'remove' will conveniently remove the value '5' from the list.

numbers.index(4)
#'index' method will return the index of the number that is asked of.

print(10 in numbers)
#This returns the boolean value. If 10 exists in the list it will be True else it'll be False.

print(numbers.count(1))
#The method of 'count' will return actually the number of numbers are there in the list.

numbers.sort()
#In the 'sort' method the numbers are simply sorted.

numbers.reverse()
#In the 'reverse' method the numbers get reversed from their last position.

print(numbers.pop(3))
#'pop' will remove the number existing in the index given and display it.

print(numbers)
print(num2)