class Mammal:
    def walk(self):
        print("Walk")
#In inheritance, here the parent class has to be defined first.
#From this parent class, the subclasses will get it's use called.

class Dog(Mammal):
    pass
#In this sub class of Dog, the function is inherited by calling in definition.
#Python still expects a code further so to notify Python there ain't any, pass is used.

class Cat(Mammal):
    pass


Tommy = Dog()
Tommy.walk()
