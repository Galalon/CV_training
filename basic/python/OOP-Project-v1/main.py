
import cv2 as cv
from colors import *
import numpy as np
from complex_shapes.neighborhood import *
from complex_shapes.city import *
from shapes.rectangle import *
from shapes.triangle import *


def main():
    
    # house  = House(RectangleFactory.create_rectangle_from_low_left_point(Point(0,0), 10, 10), 5)
    # house.draw()

    img = np.zeros((1000,1000,3), np.uint8)

    
    # rec = Rectangle(Point(100, 100), 100, 100, RED, GREEN)
    # tri = Triangle(Point(200, 200), Point(300, 200), Point(250, 100), CYAN, MAGENTA)
    # tri2 = Triangle(Point(300, 300), Point(300, 200), Point(250, 100), RED, YELLOW)
    # circle1 = Circle(Point(100, 100), 50, RED, GREEN)
    # tri.draw(img)
    # tri2.draw(img)
    # rec.draw(img)
    # circle1.draw(img)

    # house_builder = HouseBuilder()
    # house_director = HouseDirector(house_builder)
    # house_director.build_simple_house(Point(200,200))
    # house = house_builder.get_product()
    # house_director.build_fancy_house(Point(600,200))
    # fancy_house = house_builder.get_product()
    # fancy_house.scale(2)
    # fancy_house.draw(img)
    # house.rotate(90)
    # house.scale(1.5)
    # house.draw(img)

    neighborgood_planner = NeighborhoodPlanner(Point(50,200))
    neighborhood = neighborgood_planner.create_fancy_neighborhood(5,)
    neighborhood.draw(img)
    neighborhood.rotate(10)
    neighborhood.translate(0, 200)
    neighborhood.draw(img)


    # city_planner = CityPlanner(Point(50, 200))
    # city = city_planner.create_simple_city(4, 5)
    # city = city_planner.create_fancy_city(4, 5)
    # city.rotate(10)
    # city.draw(img)

    # rectangle = Rectangle(Point(400,400), 100, 100, RED, GREEN)
    # rectangle.draw(img)
    # rectangle.translate(200,-200)
    # rectangle.scale(1.5)
    # rectangle.draw(img)
    # rectangle.translate(200,-200)
    # rectangle.rotate(45)
    # rectangle.draw(img)
    # rectangle.translate(200,-200)
    # rectangle.rotate(45)
    # rectangle.draw(img)
    # rectangle1 = Rectangle(Point(200,200), 200, 100, RED, GREEN)
    # rectangle1.translate(200, -200)
    # rectangle1.rotate(100)
    # rectangle1.draw(img)

    # triangle = Triangle(Point(200, 200), Point(400, 200), Point(300, 100), CYAN, MAGENTA)
    # triangle = RectangleFactory.create_rectangle_from_low_left_point(Point(200,200), 100, 100, RED, GREEN)
    # triangle.draw(img)
    # triangle.translate(100, -100)
    # triangle.rotate(90)
    # triangle.draw(img)
    # triangle.translate(100, -100)
    # triangle.rotate(90)
    # triangle.draw(img)
    # triangle.translate(100, -100)
    # triangle.rotate(135)
    # triangle.draw(img)
    # triangle.translate(100, -100)
    # triangle.rotate(180)
    # triangle.draw(img)



    cv.imshow('RGB', img)

    # cv.imshow('RGB', img)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()

    