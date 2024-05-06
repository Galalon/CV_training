from complex_shapes.house import House, HouseBuilder, HouseDirector
from complex_shapes.complex_shape import ComplexShape
from shapes.point import Point
from shapes.shape import Shape



class Neighborhood(ComplexShape):
    def __init__(self, ):
        super().__init__([])

    def add_house(self, house: Shape):
        self._add_shape(house)

    def rotate_by_center(self, center_point: Point, angle: float):
        return super().rotate_by_center(center_point, angle)
    
    def rotate(self, angle: float):
        # center house is the median index
        center_house = self._shapes[len(self._shapes) // 2]
        center_point = center_house.get_center_point()
        self.rotate_by_center(center_point, angle)


class NeighborhoodPlanner:
    def __init__(self, low_left_point):
        self.low_left_point = low_left_point
        self.lot_length = 150
        self.house_builder = HouseBuilder()
        self.house_director = HouseDirector(self.house_builder)


    def create_simple_neighborhood(self, num_houses: int) -> Neighborhood:
        neighborhood = Neighborhood()
        for i in range(num_houses):
            self.house_director.build_simple_house(self.low_left_point  + (i * self.lot_length, 0))
            house = self.house_builder.get_product()
            neighborhood.add_house(house)

        return neighborhood
    
    def create_fancy_neighborhood(self, num_houses: int) -> Neighborhood:
        neighborhood = Neighborhood()
        for i in range(num_houses):
            self.house_director.build_fancy_house(self.low_left_point  + (i * self.lot_length, 0))
            house = self.house_builder.get_product()
            neighborhood.add_house(house)

        return neighborhood
    


        