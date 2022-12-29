import abc

import numpy as np


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self, image_to_draw_on: np.ndarray) -> np.ndarray:
        """

        :param image_to_draw_on: The image to draw the shape on
        :return: The image after the shape was drawn
        """
        pass

    @abc.abstractmethod
    def rotate(self, angle: float, center=(0, 0)) -> None:
        """

        :param angle: angle to rate - in degrees - clockwise
        :param center: the center of the shape - the point to rotate around
        :return: No return object - changes the object attributes
        """
        pass

    @abc.abstractmethod
    def translate(self, horizontal: int, vertical: int) -> None:
        """

        :param horizontal: horizontal delta to move the shape - positive to the right, negative to the left
        :param vertical: horizontal delta to move the shape - positive down, negative up
        :return: No return object - changes the object attributes
        """
        pass

    @abc.abstractmethod
    def resize(self, factor: float, center=(0, 0)) -> None:
        """

        :param factor: resize factor
        :param center: he center of the shape - the point to resize around
        :return: No return object - changes the object attributes
        """
        pass
