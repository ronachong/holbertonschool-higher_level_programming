from math import pi

class Circle:
    def __init__(self, radius):
        self.name = "unnamed" # initialize as unnamed
        self.__radius = radius
        self.__center = [0, 0] # initialize at 0, 0
        self.__color = "white" # initialize at white

    def set_center(self, list):
        self.__center = list
        return

    def get_center(self):
        return self.__center

    def set_color(self, string):
        self.__color = string
        return

    def get_color(self):
        return self.__color

    def area(self):
        return pi*self.__radius*self.__radius
    
