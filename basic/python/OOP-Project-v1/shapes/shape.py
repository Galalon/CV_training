from matplotlib import pyplot as plt
from shapes.point import Point
import cv2 as cv
from colors import *
import numpy as np

# Interface for shape
class Shape:
        
    def draw(self, img:plt.figure):
       raise NotImplementedError("Subclass must implement abstract method")
    
    def rotate_by_center(self, center_point:Point, angle: float):
        raise NotImplementedError("Subclass must implement abstract method")

    def rotate(self, angle: float):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def translate(self, x: int, y: int):
        raise NotImplementedError("Subclass must implement abstract method")
        
    def scale(self, factor: float):
        raise NotImplementedError("Subclass must implement abstract method")
        
    def get_center_point(self):
        raise NotImplementedError("Subclass must implement abstract method")
        

