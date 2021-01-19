class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #With init method one can initialize the object.
        #It is known as Constructor.
        #self here references the self values of the point that will be used later.

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point = Point(10, 20)
#In this, the point has two parameters. These have been previously defined by the Constructor init.
print(point.x)