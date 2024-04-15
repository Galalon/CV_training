from complex_shapes.neighborhood import Neighborhood, NeighborhoodPlanner
from complex_shapes.complex_shape import ComplexShape

class City(ComplexShape):
    def __init__(self, ):
        super().__init__([])

    def add_neighborhood(self, neighborhood: Neighborhood):
        self._add_shape(neighborhood)




class CityPlanner:
    def __init__(self, low_left_point):
        self.low_left_point = low_left_point # low left point of the first house (top left house)
        self.neighborhood_height = 200

    def create_simple_city(self, num_neighborhoods: int, num_houses: int) -> City:
        next_low_left_point = self.low_left_point
        city = City()
        for i in range(num_neighborhoods):
            neighborhood_planner = NeighborhoodPlanner(next_low_left_point)
            neighborhood = neighborhood_planner.create_simple_neighborhood(num_houses)
            city.add_neighborhood(neighborhood)

            next_low_left_point = next_low_left_point + (0, self.neighborhood_height)


        return city

    def create_fancy_city(self, num_neighborhoods: int, num_houses: int) -> City:
        next_low_left_point = self.low_left_point
        city = City()
        for i in range(num_neighborhoods):
            neighborhood_planner = NeighborhoodPlanner(next_low_left_point)
            neighborhood = neighborhood_planner.create_fancy_neighborhood(num_houses)
            city.add_neighborhood(neighborhood)

            next_low_left_point = next_low_left_point + (0, self.neighborhood_height)

        return city

    def create_mixed_city(self, num_neighborhoods: int, num_houses: int) -> City:
        next_low_left_point = self.low_left_point
        city = City()
        # every other neighborhood is fancy
        for i in range(num_neighborhoods):
            neighborhood_planner = NeighborhoodPlanner(next_low_left_point)
            if i % 2 == 0:
                neighborhood = neighborhood_planner.create_fancy_neighborhood(num_houses)
            else:
                neighborhood = neighborhood_planner.create_simple_neighborhood(num_houses)
            city.add_neighborhood(neighborhood)

            next_low_left_point = next_low_left_point + (0, self.neighborhood_height)

        return city
