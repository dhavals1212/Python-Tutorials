Phone = input("Your number: ")
digits={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Sevem",
    "8":"Eight",
    "9":"Nine",
    "0":"Zero"
}

output = ""
for ch in Phone:
    output += digits.get(ch) + " "
print(f"The number you have dialed is {output}")