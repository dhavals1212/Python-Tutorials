Capiche = "oola lala la le O"
print(len(Capiche))
#Here the 'len' function prints the length of the string in numbers.

print(Capiche.lower())
#For other additional operations one can use '.' after a variable to see those operations.
#Here we chose 'lower' which is an operation that creates the new string in lower case.

print(Capiche.upper())
#In here, it will be another string in all upper case letters.

print(Capiche.find("O"))
#The 'find' operation will find the designated character 'O' in here.
#Here it will be the first string, so it will index the number in the print.
#If there weren't any 'O' in the string the result would be -1.

print(Capiche.find("la"))
#Here the find operation will return 'la' index which is 2.

print(Capiche.replace("O", "O oola lala la le O"))
#The replace operation will replace the 'O' with the one being replaced.
#Syntax here is variable.replace(original, replaced string)

print("lala" in Capiche)
#'in' command actually looks for mentioned 'lala' in Capiche.
#If it does exist there it will return True else, it'll return False.
#Remember that it is all case sensitive. A 'LALA', 'Lala' or 'laLA' will produce the output to be False.
#'find' method will return the index value as output whereas 'in' method will return boolean value.

print(Capiche.title())
#'title' operation will return the output string with first letter of every word in capital case letter.

print(Capiche.capitalize())
#In here, 'capitalize will make the first letter capital and all else lower case.