class Car:
    def __init__(self, *args, **kwargs):
        if name == "" or type(name) != str:
            raise Exception("name is not a string")
        if brand == "" or type(brand) != str:
            raise Exception("brand is not a string")
        if type(nb_doors) != int or nb_doors <= 0:
            raise Exception("nb_doors is not > 0")

        
