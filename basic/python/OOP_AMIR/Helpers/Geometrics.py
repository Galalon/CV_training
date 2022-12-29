import math
from typing import Tuple


# Namespace
class Geometrics:

    @staticmethod
    def rotate(point_to_rotate_around: Tuple[float, float], point_to_rotate: Tuple[float, float], angle_in_rad: float) \
            -> Tuple[float, float]:
        """
        Rotates a point around another: used this source to implement
        https://math.stackexchange.com/questions/1725790/calculate-third-point-of-triangle-from-two-points-and-angles
        :param point_to_rotate_around: the point to do the rotation around
        :param point_to_rotate: the point to rotate around point_to_rotate_around
        :param angle_in_rad: the angle to rotate - clockwise
        :return: the new coordinates of the rotated point
        """
        if point_to_rotate == point_to_rotate_around:
            return point_to_rotate
        new_angle_in_rad = angle_in_rad
        if angle_in_rad > math.pi:
            new_angle_in_rad = (2 * math.pi) - new_angle_in_rad
        other_angle = math.pi / 2 - new_angle_in_rad / 2
        u = point_to_rotate_around[0] - point_to_rotate[0]
        v = point_to_rotate_around[1] - point_to_rotate[1]
        a3 = math.sqrt(u ** 2 + v ** 2)
        a2 = a3 * math.sin(new_angle_in_rad) / math.sin(other_angle)
        rhs1 = point_to_rotate[0] * u + point_to_rotate[1] * v + a2 * a3 * math.cos(other_angle)
        rhs2 = point_to_rotate_around[1] * u - point_to_rotate_around[0] * v + a2 * a3 * math.sin(other_angle)
        if angle_in_rad < math.pi:
            rhs2 = point_to_rotate_around[1] * u - point_to_rotate_around[0] * v - a2 * a3 * math.sin(other_angle)
        return (1 / (a3 ** 2)) * (u * rhs1 - v * rhs2), (1 / (a3 ** 2)) * (v * rhs1 + u * rhs2)

    @staticmethod
    def resize(point_to_resize_around: Tuple[float, float], point_to_move: Tuple[float, float], resize_factor: float) \
            -> Tuple[float, float]:
        """

        :param point_to_resize_around: the point to do the resize around
        :param point_to_move: the point to move around point_to_resize_around
        :param resize_factor: the factor of resize
        :return: the new coordinates of the point
        """
        delta_x = point_to_move[0] - point_to_resize_around[0]
        delta_y = point_to_move[1] - point_to_resize_around[1]
        new_delta_x = resize_factor * delta_x
        new_delta_y = resize_factor * delta_y
        return (point_to_resize_around[0] + new_delta_x), (point_to_resize_around[1] + new_delta_y)

    @staticmethod
    def translate(point_to_translate: Tuple[float, float], delta_x: float, delta_y: float) -> Tuple[float, float]:
        """

        :param point_to_translate: the point to move
        :param delta_x: horizontal translation
        :param delta_y: vertical translation
        :return: the new coordinates of the translated point
        """
        return (point_to_translate[0] + delta_x), (point_to_translate[1] + delta_y)
