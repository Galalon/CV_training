# from ParsersAndDrawers.JSONParser import JSONParser
import matplotlib.pyplot as plt

from OOP.OOP_EX.OOP_EX.ParsersAndDrawers.JSONParser import JSONParser


class DrawerFromJSON:

    def __init__(self, image_to_draw_on):
        self._image_to_draw_on = image_to_draw_on
        self._parser = JSONParser()

    def draw(self, json_file_path: str) -> None:
        """

        :param json_file_path: the json path describing what to draw
        :return: No return object, the method directly plot the drawing
        """
        shape_to_draw = self._parser.parse(json_file_path)
        shape_to_draw.translate(self._image_to_draw_on.shape[1] // 2, self._image_to_draw_on.shape[0] // 2)
        plt.imshow(shape_to_draw.draw(self._image_to_draw_on))
        plt.show()
