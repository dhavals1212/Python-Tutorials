customer = {
    "name": "Dhaval Shukla",
    "age": 24,
    "is_goodguy": True
}
#This is a dictionary.
#In the dictionary the parent key values such as 'name', 'age' and 'is_goodguy' is always unique.
#Moreover, dictionary can contain any value and store it may it be boolean, list or tuple, character or number.
#To define the parent and child value, it is written as "parent" : child
#Dictionary parent values are case sensitive.

print(customer["age"])
#To get the dictionary value, one must use square brackets and write the parent entity as index as is.

print(customer.get("name"))
#'get' will get the value of the key.

print(customer.get("birthdate", "Dec 12 1996"))
#'get' can also be used to add a temporary parent and child key to the dictionary until the value is returned.

customer["name"] = "Jack Smith"
#This will replace the child key value with the value defined above.

customer["birthdate"] = "Dec 12 1996"
#this will simply add a parent and child key to the dictionary.

print(customer)