#we use classes to define new types in python
# like a shopping cart its not any type we used before
# define new type called point
#point.move/draw/get_distance(from another point)
class Point: #pacsal naming convention
    def move(self):
        print("move")
    def draw(self):
        print("draw") #DONT FORGET THE 2 LINES BREAK



    #naming classes is different than naming variable or strings
    # we dont use underscore or anything else we capatalize the first letter of the word if we want to write multiple words
#class PointRev zy heek!
#OBJECTS ARE THE ACTUAL INSTANCES OF A BLUEPRINT
point1 = Point()
point2 = Point()#storing the object in a variable
point1.draw() #later on will discover the magic expand
#they also have attributes and those attributes are like variables that belongs to a particular object
point1.x = 1
point2.y = 5
print(point1.x, point2.y)
#we use (contructors) to help the problem of undefined x and y which doesnt make
#sense when we talk about points i need to know where its located
