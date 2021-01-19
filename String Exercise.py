cool = "All hail Nikola Tesla"
#We can save a string simply without writing print command if we use the "" here.

print(cool[0])
#Here the [0] will print only the first letter in the string cool.

print(cool[-1])
#In python -1 indicates the last character of that string. This will display 'a' character.

print(cool[0:4])
#Here as we can see the index defines from which point to which point we want our output.
#0 to 4 will print the range of characters from 'All ' as they are.
#It will exclude the 4th string character in this.

print(cool[0:])
#Since there has been no last range number shown here, it will print all the string values.

print(cool[:-1])
#As the code again goes same will happen with endless range of left side to the -1 which is last character.
#Although -1 itself will be excluded, which means last character won't be printed.

print(cool[:])
#Simply putting ':' here will print the string as is.

message = f'{cool} is my belief.'
#Writing in "f''" makes it a formatted string.
#With help of formatted strings the coding becomes easier.
#The {} here are placeholders for the variables assigned and called in the code.
#Here the 'cool' was called so in formatted string it had to be written in {}.

print(message)