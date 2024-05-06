import numpy as np

class Point:
    
    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)

    def get_tuple(self):
        return (self.x, self.y)
    
    # angle is clockwise (formula is for counter clockwise but the y axis is flipped so it is clockwise angle)
    def rotate(self, center_point, angle):

        # flip y axis
        # center_point = Point(center_point[0], -center_point[1])
        # self.y = -self.y

        # rotate according to origin normally
        x = self.x - center_point.x
        y = self.y - center_point.y 

        # angle = - angle
        angle = np.deg2rad(angle)

        x_new = x * np.cos(angle) - y * np.sin(angle)
        y_new = x * np.sin(angle) + y * np.cos(angle)
        

        self.x = int(x_new + center_point.x) 
        self.y = int(y_new + center_point.y)

        # flip y axis back
        # self.y = -self.y

    def scale(self, center_point, factor):
        x = self.x - center_point.x
        y = self.y - center_point.y

        x_new = x * factor
        y_new = y * factor

        self.x = int(x_new + center_point.x)
        self.y = int(y_new + center_point.y)

    def translate(self, x: int, y: int):
        self.x += x
        self.y += y


    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range")

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    