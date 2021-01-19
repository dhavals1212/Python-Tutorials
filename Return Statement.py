def square(number):
    return number * number
#Here, 'return' returns the coded purpose of the squre function whenever it will be called.

def squared(number):
    print(number * number)
    return None
#By default every function returns 'None' value, it can be changed.


result = square(3)
print(result)

print(squared(3))