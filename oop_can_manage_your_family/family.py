class Person:

    # define class attributes
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]
    
    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        # define object attributes
        self.__id = id
        self.__first_name = first_name
        self.last_name = "[unassigned]"
        self.__date_of_birth = date_of_birth
        self.__genre = genre
        self.__eyes_color = eyes_color
        
        # set cases to raise exceptions
        if id < 0 or type(id) != int:
            raise Exception("id is not an integer")
        if first_name == "" or type(first_name) != str:
            raise Exception("string is not a string")
        if type(date_of_birth) != list or len(date_of_birth) != 3:
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[0] not in range(1, 13):
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[1] not in range(1, 32):
            raise Exception("date_of_birth is not a valid date")
        if type(date_of_birth[2]) != int:
            raise Exception("date_of_birth is not a valid date")
        if type(genre) != str or genre not in Person.GENRES:
            raise Exception("genre is not valid")
        if type(eyes_color) != str or eyes_color not in Person.EYES_COLORS:
            raise Exception("eyes_color is not valid")
        pass
    
    # define getter functions
    def get_id(self):
        return self.__id
    def get_first_name(self):
        return self.__first_name
    def get_date_of_birth(self):
        return self.__date_of_birth
    def get_genre(self):
        return self.__genre
    def get_eyes_color(self):
        return self.__eyes_color
