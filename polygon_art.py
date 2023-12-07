import turtle
import random

class Drawer:
    """
    This class is used to draw a single polygon.
    """
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)

    def __random_state(self):
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
        self.__draw_polygon_base_mothod(num_sides)
        for _ in range(2):
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
        turtle.penup()

class Options:
    def __init__(self):
        self.__drawer = Drawer()

    def __option_1(self, num):
        for _ in range(num):
            self.__drawer.draw_simple_polygon(3)

    def __option_2(self, num):
        for _ in range(num):
            self.__drawer.draw_simple_polygon(4)

    def __option_3(self, num):
        for _ in range(num):
            self.__drawer.draw_simple_polygon(5)
    
    def __option_4(self, num):
        for _ in range(num):
            num_sides = random.randint(3, 5) # triangle, square, or pentagon
            self.__drawer.draw_simple_polygon(num_sides)

    def __option_5(self, num):
        for _ in range(num):
            self.__drawer.draw_complex_polygon(3)

    def __option_6(self, num):
        for _ in range(num):
            self.__drawer.draw_complex_polygon(4)

    def __option_7(self, num):
        for _ in range(num):
            self.__drawer.draw_complex_polygon(5)
    
    def __option_8(self, num):
        for _ in range(num):
            num_sides = random.randint(3, 5) # triangle, square, or pentagon
            self.__drawer.draw_complex_polygon(num_sides)

    def choose(self, option, num = 20):
        if num == "":
            num = 20
        num_int = int(num)
        if num_int <= 0:
            raise ValueError("Numbers of polygon must be bigger than 0")
        if option == 1:
            self.__option_1(num_int)
        elif option == 2:
            self.__option_2(num_int)
        elif option == 3:
            self.__option_3(num_int)
        elif option == 4:
            self.__option_4(num_int)
        elif option == 5:
            self.__option_5(num_int)
        elif option == 6:
            self.__option_6(num_int)
        elif option == 7:
            self.__option_7(num_int)
        elif option == 8:
            self.__option_8(num_int)
        else:
            raise ValueError("Options only contain 1-8")



_input = int(input("Which art do you want to generate? Enter a number between 1 to 8, inclusive: "))

num = random.randint(20, 50) # In case you want to specified the number of polygons your self, you can do it here.
options = Options()
options.choose(_input, num)

turtle.done()