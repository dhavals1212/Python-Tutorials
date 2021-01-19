def emoji_converter(message):
    words = Message.split(' ')

    emoji = {
        ":)": "🙂",
        ":(": "😔",
        ":D": "😁",
        ";)": "😉",
        ":": "😶",
        ":o": "😮"
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output
#In this, the whole message body will be used to define message.
#'return' is used to return the output.


Message = input(">>")
print(emoji_converter(Message))
#As soon as the above function gets executed, because of the return output statement, it will be returned accordingly.
#This is a prime example of a reusable function.