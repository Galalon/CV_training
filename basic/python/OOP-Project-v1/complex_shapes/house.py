from complex_shapes.complex_shape import ComplexShape
from shapes.rectangle import Rectangle, RectangleFactory
from shapes.triangle import Triangle
from shapes.point import Point
from shapes.circle import Circle
from colors import *

class House(ComplexShape):

    def __init__(self, low_left_point: Point):
        #super init
        self._low_left_point = low_left_point
        super().__init__([])

    def set_body(self, width: float, height: float,  color:RGB = BLUE, fill_color:RGB = BLUE):
        self.house_body = RectangleFactory.create_rectangle_from_low_left_point(self._low_left_point, width, height, color, fill_color)
        self.roof_base_y = self._low_left_point[1] - height - BORDER_THICKNESS

        self._add_shape(self.house_body)

    def set_roof(self, roof_height: float, roof_color:RGB = RED, roof_fill_color:RGB = RED):
        roof_point_y =self.roof_base_y - roof_height
        left_point_x = self._low_left_point[0]
        right_point_x = self._low_left_point[0] + self.house_body.width

        roof_left_point = Point(left_point_x, self.roof_base_y)
        roof_right_point = Point(right_point_x, self.roof_base_y)
        roof_top_point = Point((roof_left_point[0] + roof_right_point[0])/2, roof_point_y)

        self.roof = Triangle(roof_left_point, roof_right_point, roof_top_point , roof_color, roof_fill_color)

        self._add_shape(self.roof)

    def set_door(self, door_color:RGB = BROWN, door_fill_color:RGB = BROWN):
        left_point_x = self._low_left_point[0]
        right_point_x = self._low_left_point[0] + self.house_body.width
        door_low_left_point = Point((left_point_x + right_point_x)/2, self._low_left_point[1])
        door_width = self.house_body.width/4
        door_height = self.house_body.height/2
        self.door = RectangleFactory.create_rectangle_from_low_left_point(door_low_left_point, door_width, door_height, door_color, door_fill_color)
        self._add_shape(self.door)

    def set_window(self, window_color:RGB = BLACK, window_fill_color:RGB = MAGENTA):
        radius = self.house_body.width/8
        # x1 = self.house_body.points["up_left"].x
        # x2 = self.house_body.points["up_right"].x
        # y1 = self.house_body.points["up_left"].y
        # y2 = self.house_body.points["low_left"].y
        left_point_x = self._low_left_point[0]
        right_point_x = self._low_left_point[0] + self.house_body.width
        x1 = left_point_x
        x2 = right_point_x
        y1 = self._low_left_point[1] - self.house_body.height
        y2 = self._low_left_point[1]

        x_window = x1 + 3*((x2 - x1)/4)
        y_window = y2 - 3*((y2 - y1)/4)
        center = Point(x_window, y_window )
        self.window = Circle(center, radius, window_color, window_fill_color)
        self._add_shape(self.window)

    def get_center_point(self):
        return self.house_body.get_center_point()

    # def scale(self, factor: float):
        

        # self.house_body.scale(factor)
        # self.roof.scale(factor)
        # self.door.scale(factor)
        # self.window.scale(factor)


    
        



        


class Builder:
    def __init__(self):
        pass

    def reset(self,low_left_point: Point):
        pass

    def set_body(self, width: float, height: float,  color:RGB, fill_color:RGB):
        pass

    def set_roof(self, roof_height: float, color:RGB, fill_color:RGB):
        pass

    def set_door(self, door_color:RGB, door_fill_color:RGB):
        pass

    def set_window(self, window_color:RGB, window_fill_color:RGB):
        pass
        
    def get_product(self,) -> House:
        pass


class HouseBuilder(Builder):
    def __init__(self):
        pass

    def reset(self, low_left_point: Point):
        self._house = House(low_left_point)

    def set_body(self, width: float, height: float,  color:RGB = WHITE, fill_color:RGB = WHITE):
        self._house.set_body(width, height, color, fill_color)

    def set_roof(self, roof_height: float, color:RGB = RED, fill_color:RGB = RED):
        self._house.set_roof(roof_height, color, fill_color)

    def set_door(self, door_color:RGB = BROWN, door_fill_color:RGB = BROWN):
        self._house.set_door(door_color, door_fill_color)

    def set_window(self, window_color:RGB = BLACK, window_fill_color:RGB = MAGENTA):
        self._house.set_window(window_color, window_fill_color)

    def get_product(self,) -> House:
        curr_house = self._house
        return curr_house 


class HouseDirector:
    def __init__(self, builder: Builder):
        self.default_width = 100
        self.default_height = 100
        self.default_roof_height = 50
        self._builder = builder

    def change_builder(self, builder: Builder):
        self._builder = builder

    def build_simple_house(self, low_left_point: Point):
        self._builder.reset(low_left_point)
        self._builder.set_body(self.default_width, self.default_height)
        self._builder.set_roof(self.default_roof_height)
        self._builder.set_door()
    
    def build_fancy_house(self, low_left_point: Point):
        self._builder.reset(low_left_point)
        self._builder.set_body(self.default_width, self.default_height, color=CYAN, fill_color=WHITE)
        self._builder.set_roof(self.default_roof_height, color=GREEN, fill_color=BROWN)
        self._builder.set_door(door_color=BLACK, door_fill_color=BROWN)
        self._builder.set_window()
    
    # I do not have a draw which violates the Liskov Substitution Principle (LSP)
    # but the draw function does exactly the same thing as the ComplexShape draw function, for now. 11/4 9:51

    
        
        


