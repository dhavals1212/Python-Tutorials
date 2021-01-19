is_it_hot = input("Is it a hot day? ")

if is_it_hot=='hot':
    #if statement is used to define a condition.
    #if a condition is true then do this or execute this.
    #Here the input is to get the input hot or cold.
    #To designate the value as 'hot' you will get a return. '==' mentions the exact value entered.
    print("It's a hot day bruh.")
    print("Drink lots of water. K?")
elif is_it_hot=='cold':
    #elif is known as 'else if'.
    #It is another general condition that targets the input and tries to know if it is true.
    #The condition if true is executed, only if the above 'if' statement is false.
    print("It's cold.")
    print("Wear a jacket or somethin'.")
else:
    #'else' statement is executed only if 'if' and 'elif' statements are not true.
    #'else' will be executed if the 'if' statement above isn't correct or entered value is different.
    print("Nobody knows bruh!")
    print("Can you pass me that bottle of watah?")
print("What're you makin'?")
#In this case, the code is exited after the indent mark is exited.
#That is denoted by the 'hourglass' looking entity that denotes beginning to end of statement and condition.
