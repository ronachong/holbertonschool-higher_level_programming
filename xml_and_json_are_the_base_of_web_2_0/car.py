class Car:
    def __init__(self, *args, **kwargs):
        print "args is equal to " + str(args)
        print "kwargs is equal to " + str(kwargs)
        '''if len(args) > 0 and isinstance(args[0], dict):
        # assuming that hash is passed as first arg
            hash = args[0]
            # get values from hash
            name = hash.get('name')
            brand = hash.get('brand')
            nb_door = hash.get('nb_door')

        if name == "" or type(name) != str:
            raise Exception("name is not a string")
        if brand == "" or type(brand) != str:
            raise Exception("brand is not a string")
        if type(nb_doors) != int or nb_doors <= 0:
            raise Exception("nb_doors is not > 0")'''
