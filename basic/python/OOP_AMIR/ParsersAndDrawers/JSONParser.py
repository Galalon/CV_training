import copy
import json
import math
from typing import Dict

from OOP.OOP_EX.OOP_EX.ParsersAndDrawers.ShapeFactoryFromJSON import ShapeFactoryFromJSON
from OOP.OOP_EX.OOP_EX.Shapes.Shape import Shape


class JSONParser:

    def __init__(self) -> None:
        self._shape_factory = ShapeFactoryFromJSON()
        self._shapesMemoization = dict()

    def __parse_dict(self, json_dict: Dict) -> Shape:
        """

        :param json_dict: Json dictionary to parse
        :return: Top Level Shape object corresponding to the highest nesting level of the main json
        """

        if 'shapeJsonPath' in json_dict:
            shape = self.parse(json_dict['shapeJsonPath'])
        else:
            shape = self._shape_factory.build_shape_from_json(json_dict)
            if "shapes" in json_dict:
                for sub_json_dict in json_dict["shapes"]:
                    sub_shape = self.__parse_dict(sub_json_dict)
                    shape.add_shape(sub_shape)
        self.__rotate_from_json(shape, json_dict)
        self.__resize_from_json(shape, json_dict)
        self.__translate_from_json(shape, json_dict)
        return shape

    def parse(self, shape_json_path: str) -> Shape:
        """
        Auxiliary parse method to deal with a json containing a path instead of concrete data.
        :param shape_json_path: the json to parse
        :return: the shape corresponding to the json with the path
        """

        if shape_json_path in self._shapesMemoization:
            return copy.deepcopy(self._shapesMemoization[shape_json_path])
        else:
            with open(shape_json_path) as json_file:
                json_dict = json.load(json_file)
                shape = self.__parse_dict(json_dict)
                self._shapesMemoization[shape_json_path] = copy.deepcopy(shape)
                return shape

    @staticmethod
    def __translate_from_json(shape, json_dict: Dict) -> None:
        """
        Auxiliary parse method to read the translation data from the json and do the corresponding translation to the
        shape object.
        :param shape: the shape to translate
        :param json_dict: the json dict with the data about the translation
        :return: No return object, the shape is directly modified
        """
        if "translationX" in json_dict:
            translation_x = json_dict["translationX"]
            translation_y = json_dict["translationY"]
            shape.translate(translation_x, translation_y)

    @staticmethod
    def __rotate_from_json(shape, json_dict: Dict) -> None:
        """
        Auxiliary parse method to read the rotate data from the json and do the corresponding rotation to the
        shape object.
        :param shape: the shape to rotate
        :param json_dict: the json dict with the data about the rotation
        :return: No return object, the shape is directly modified
        """
        if "rotate_angle" in json_dict:
            rotate_angle = math.radians(json_dict["rotate_angle"])
            shape.rotate(rotate_angle)

    @staticmethod
    def __resize_from_json(shape, json_dict: Dict) -> None:
        """
        Auxiliary parse method to read the resize data from the json and do the corresponding resize to the
        shape object.
        :param shape: the shape to resize
        :param json_dict: the json dict with the data about the resize
        :return: No return object, the shape is directly modified
        """
        if "resize" in json_dict:
            resize_factor = json_dict["resize"]
            shape.resize(resize_factor)
