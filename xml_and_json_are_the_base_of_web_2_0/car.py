class Car:
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            # assume that kwargs is the hash of properties
            hash = kwargs
            # get values from hash
            name = hash.get('name')
            brand = hash.get('brand')
            nb_doors = hash.get('nb_doors')

        # raise exceptions given improper argument values
        if name == "" or type(name) != str:
            raise Exception("name is not a string")
        if brand == "" or type(brand) != str:
            raise Exception("brand is not a string")
        if type(nb_doors) != int or nb_doors <= 0:
            raise Exception("nb_doors is not > 0")

        # else set private attributes according to parameters
        self.__name = name
        self.__brand = brand
        self.__nb_doors = nb_doors
