import json
from xml.dom import minidom
from xml import sax

class Car:
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            # assume that kwargs is the hash of attributes
            hash = kwargs
        elif len(*args) > 0 and isinstance(args[0], dict):
            # assume that args is hash of attributes
            hash = args[0]
            
        # get values from hash
        name = hash.get('name')
        brand = hash.get('brand')
        nb_doors = hash.get('nb_doors')

        # raise exceptions given improper argument values
        if name == "" or type(name) != unicode:
            raise Exception("name is not a string")
        if brand == "" or type(brand) != unicode:
            raise Exception("brand is not a string")
        if type(nb_doors) != int or nb_doors <= 0:
            raise Exception("nb_doors is not > 0")

        # else set private attributes according to parameters
        self.__name = name
        self.__brand = brand
        self.__nb_doors = nb_doors

    # getter instance methods
    def get_name(self):
        return self.__name

    def get_brand(self):
        return self.__brand

    def get_nb_doors(self):
        return self.__nb_doors

    # setter instance method
    def set_nb_doors(self, number):
        self.__nb_doors = number

    # other instance methods
    def to_hash(self):
        return {'name': self.__name, 'brand': self.__brand, 'nb_doors': self.__nb_doors}

    def to_json_string(self):
        return json.dumps(self.to_hash())

    def to_xml_node(self, doc):
        car_element = doc.createElement('car')
        car_element.setAttribute('nb_doors', str(self.__nb_doors))
        doc.appendChild(car_element)

        name_element = doc.createElement('name')
        name_content = doc.createCDATASection(self.__name)
        name_element.appendChild(name_content)
        car_element.appendChild(name_element)

        brand_element = doc.createElement('brand')
        brand_content = doc.createTextNode(self.__brand)
        brand_element.appendChild(brand_content)
        car_element.appendChild(brand_element)

        return car_element

    def __str__(self):
        return self.__name + " " + self.__brand + " (" + str(self.__nb_doors) + ")"
