import sys

import numpy as np

sys.path+=['..']
from OOP.OOP_EX.OOP_EX.ParsersAndDrawers.DrawerFromJSON import DrawerFromJSON

if __name__ == '__main__':
    json_img_to_draw_on3 = np.ones((500, 500, 3), np.uint8) * 255
    drawer = DrawerFromJSON(json_img_to_draw_on3)
    drawer.draw('../DataForTest/TrafficLightAndTriangleRotated.json')

    json_img_to_draw_on4 = np.ones((3000, 2100, 3), np.uint8) * 195
    drawer = DrawerFromJSON(json_img_to_draw_on4)
    drawer.draw('../DataForTest/City.json')
