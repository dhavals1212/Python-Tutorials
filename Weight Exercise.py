print("Welcome to weight conversion board:")
weight_input = input("What's your weight in pounds? ")
weight_kg = int(weight_input) * 0.45
#Here the 'int' indicates the integer operation done on the 'weight_kg' variable.
#Since python can't recognise the 'weight_input' because the input becomes a string, it has to be converted.
#Hence, 'int', 'float' or 'str' are the commands used.
#int command is for integer value, float for float and str for characters.
#bool command is for boolean values.

print("Your weight in pounds is " + weight_input + " lbs")
print("Your weight in kgs is " + str(weight_kg) + " kgs")
#Since we have denoted weight_kg variable in int value, it becomes integer.
#So, we define that in print by converting it to string by str command here.