import turtle
import random

class Drawer:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)

    def __random_state(self):
        self.__num_sides = random.randint(3, 5) # triangle, square, or pentagon
        self.__size = random.randint(50, 150)
        self.__orientation = random.randint(0, 90)
        self.__location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.__border_size = random.randint(1, 10)
        pass

    def __draw_polygon_base_mothod(self, num_sides):
        self.__num_sides = num_sides
        turtle.penup()
        turtle.goto(self.__location[0], self.__location[1])
        turtle.setheading(self.__orientation)
        turtle.color(self.__color)
        turtle.pensize(self.__border_size)
        turtle.pendown()
        for _ in range(self.__num_sides):
            turtle.forward(self.__size)
            turtle.left(360/self.__num_sides)
        turtle.penup()

    def __get_new_color(self):
        self.__color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw_simple_polygon(self, num_sides):
        self.__random_state()
        self.__get_new_color()
        self.__draw_polygon_base_mothod(num_sides)
        
    def draw_complex_polygon(self, num_sides, reduction_ratio = 0.618):
        self.__random_state()
        self.__get_new_color()
        for _ in range(3):
            # reposition the turtle and get a new location
            turtle.penup()
            turtle.forward(self.__size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(self.__size*(1-reduction_ratio)/2)
            turtle.right(90)
            self.__location[0] = turtle.pos()[0]
            self.__location[1] = turtle.pos()[1]

            # adjust the size according to the reduction ratio
            self.__size *= reduction_ratio

            # draw the second polygon embedded inside the original 
            self.__draw_polygon_base_mothod(num_sides)

drawer = Drawer()
drawer.draw_complex_polygon(3)

# def draw_polygon(num_sides, size, orientation, location, color, border_size):
#     """
#     This thing draws a polygon, only one
#     """
#     turtle.penup()
#     turtle.goto(location[0], location[1])
#     turtle.setheading(orientation)
#     turtle.color(color)
#     turtle.pensize(border_size)
#     turtle.pendown()
#     for _ in range(num_sides):
#         turtle.forward(size)
#         turtle.left(360/num_sides)
#     turtle.penup()
# 
# def get_new_color():
#     return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# 
# turtle.speed(0)
# turtle.bgcolor('black')
# turtle.tracer(0)
# turtle.colormode(255)
# 
# # draw a polygon at a random location, orientation, color, and border line thickness
# num_sides = random.randint(3, 5) # triangle, square, or pentagon
# size = random.randint(50, 150)
# orientation = random.randint(0, 90)
# location = [random.randint(-300, 300), random.randint(-200, 200)]
# color = get_new_color()
# border_size = random.randint(1, 10)
# draw_polygon(num_sides, size, orientation, location, color, border_size)
# 
# # specify a reduction ratio to draw a smaller polygon inside the one above
# reduction_ratio = 0.618
# 
# # reposition the turtle and get a new location
# turtle.penup()
# turtle.forward(size*(1-reduction_ratio)/2)
# turtle.left(90)
# turtle.forward(size*(1-reduction_ratio)/2)
# turtle.right(90)
# location[0] = turtle.pos()[0]
# location[1] = turtle.pos()[1]
# 
# # adjust the size according to the reduction ratio
# size *= reduction_ratio
# 
# # draw the second polygon embedded inside the original 
# draw_polygon(num_sides, size, orientation, location, color, border_size)
# 
# # hold the window; close it by clicking the window close 'x' mark
turtle.done()