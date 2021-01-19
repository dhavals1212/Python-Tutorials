class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi! I am {self.name}")
        #Here, 'self.name' is used to call the above variable defining which will print the name when executed.


handsome = Person("Dhaval Shukla")
handsome.talk()