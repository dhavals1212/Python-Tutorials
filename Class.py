class Point:
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point1 = Point()
#Here 'point1' is an object that is an instance of the Point() class as defined above.

point1.x = 10
#'point1.x' becomes an attribute to the object point1.

point1.y = 20
print(point1.x)
point1.draw()
#In here the draw attribute is the function of the point1 onject that was created and calls it.
#Each object is different and has different instances. Therefore, all methods for point2 differ from point1.

#Here the 'Point' has 'P' capitalized because of Pascal Naming Convention.
# #For more words, the start character will be capitalized. For example PointBlank.
#Self is a special keyword that's automatically added to the defined function under class.