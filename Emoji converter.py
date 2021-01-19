Message = input(">>")
words = Message.split(' ')
#'split' will find the way to split the written input into several different outputs.

emoji = {
    ":)": "🙂",
    ":(": "😔",
    ":D": "😁",
    ";)": "😉",
    ":" : "😶",
    ":o": "😮"
}
output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)