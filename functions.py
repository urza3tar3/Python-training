#to organizze the code
#a container to proccess a code
#break into chunks
def greet_user():
    print("Hello World!")
    print("what are you eating for launch?")


print("start")
greet_user()
# we can use parameter to customize the functions even more
def suhoor(food):
    meal = food
    print(f"{meal} is a healthy meal would keep u full!")
suhoor('batata')#positional argument
#parameters are place holders we use to define in our functions for recieving information
#argument are the actual piece of infotrmation we use to supply the funtion
#positional arugments also 3na keyword arugemnts
#which we dont care about the position there
suhoor(food='batata')#keyword argument much easier to track and to understand
