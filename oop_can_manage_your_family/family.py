import json
import os

# global functions
def save_to_file(list, filename):
    json_data = []
    # loop through list of Person instances;
    # create a hash of attr.'s from each instance;
    # and append each hash to json_data
    for x in list:
        hash = x.json()
        json_data.append(hash)
    # encode json_data & save to file
    with open(filename, 'w') as outfile:
        json.dump(json_data, outfile)

def load_from_file(filename):
    if type(filename) != str or os.path.isfile(filename) != True:
        raise Exception("filename is not valid or doesn't exist")
    with open(filename) as data_file:
        json_data = json.load(data_file)
    # initilize list
    list = []
    for x in json_data:
        if x['kind'] == "Baby":
            # initialize Baby object
            person = Baby(1, "foo", [1,01,0000], "Female", "Blue")
        elif x['kind'] == "Teenager":
            # initialize Teenager object
            person = Teenager(1, "foo", [1,01,0000], "Female", "Blue")
        elif x['kind'] == "Adult":
            # initialize Adult object
            person = Adult(1, "foo", [1,01,0000], "Female", "Blue")
        else:
            # initialize Senior object
            person = Senior(1, "foo", [1,01,0000], "Female", "Blue")
        # set attributes for object from hash
        person.load_from_json(x)
        list.append(person)
    return list

class Person:
    # define class attributes
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        # define object attributes
        self.__id = id
        self.__first_name = first_name
        self.last_name = ""
        self.__date_of_birth = date_of_birth
        self.__genre = genre
        self.__eyes_color = eyes_color
        self.is_married_to = 0
        self.children = []

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

    # define other instance functions
    def __str__(self):
        return self.__first_name + " " + self.last_name

    def __gt__(self, other):
        return Person.age(self) > Person.age(other)

    def __lt__(self, other):
        return Person.age(self) < Person.age(other)

    def __ge__(self, other):
        return Person.age(self) >= Person.age(other)

    def __le__(self, other):
        return Person.age(self) <= Person.age(other)

    def __eq__(self, other):
        return Person.age(self) == Person.age(other)

    def __ne__(self, other):
        return Person.age(self) != Person.age(other)

    def is_male(self):
        if self.__genre == "Male":
            return True

    def age(self):
        years = 2016 - self.__date_of_birth[2]
        if self.__date_of_birth[0] > 5:
            return years - 1
        if self.__date_of_birth[0] == 5 and self.__date_of_birth[1] <= 20:
                return years - 1
        else:
            return years

    def is_married(self):
        if self.is_married_to != 0:
            return True
        else:
            return False

    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0

    def just_married_with(self, p):
        if self.is_married() == True or p.is_married() == True:
            raise Exception("Already married")
        if self.can_be_married() == False or p.can_be_married() == False:
            raise Exception("Can't be married")
        self.is_married_to = p.__id
        p.is_married_to = self.__id
        if self.__genre == "Female" and p.__genre == "Male":
            self.last_name = p.last_name
        elif self.genre == "Male" and p.__genre == "Female":
            p.last_name = self.last_name

    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
        if p is None or (p.__class__.__name__ != 'Adult' and p.__class__.__name__ != 'Senior'):
            raise Exception("p is not an Adult or Senior")
        if self.can_have_child == False or p.can_have_child == False: # check for p seems redundant
            raise Exception("Can't have baby")
        if id < 0 or type(id) != int:
            raise Exception("id is not an integer")
        if first_name == "" or type(first_name) != str:
            raise Exception("string is not a string")
        if type(date_of_birth) != list:
            raise Exception("date_of_birth is not a valid date")
        for x in date_of_birth:
            if type(x) != int:
                raise Exception("date_of_birth is not a valid date")
        if type(genre) != str or genre not in Person.GENRES:
            raise Exception("genre is not valid")
        if type(eyes_color) != str or eyes_color not in Person.EYES_COLORS:
            raise Exception("eyes_color is not valid")
        self.children.append(id)
        p.children.append(id)
        return Baby(id, first_name, date_of_birth, genre, eyes_color)

    def adopt_child(self, c):
        if self.can_have_child == False:
            raise Exception("Can't adopt child")
        self.children.append(c.get_id())

    # json methods
    def json(self):
        return {'kind': self.__class__.__name__,
                'id': self.__id,
                'eyes_color': self.__eyes_color,
                'genre': self.__genre,
                'date_of_birth': self.__date_of_birth,
                'first_name': self.__first_name,
                'last_name': self.last_name,
                'is_married_to': self.is_married_to,
                'children': self.children
                }

    def load_from_json(self, json):
        if type(json) != dict:
            raise Exception("json is not valid")
        self.__id = json['id']
        self.__eyes_color = json['eyes_color']
        self.__genre = json['genre']
        self.__date_of_birth = json['date_of_birth']
        self.__first_name = json['first_name']
        self.__last_name = json['last_name']


class Baby(Person):
    def can_run(self):
        return False

    def need_help(self):
        return True

    def is_young(self):
        return True

    def can_vote(self):
        return False

    def can_be_married(self):
        return False

    def can_have_child(self):
        return False


class Teenager(Person):
    def can_run(self):
        return True

    def need_help(self):
        return False

    def is_young(self):
        return True

    def can_vote(self):
        return False

    def can_be_married(self):
        return False

    def can_have_child(self):
        return False


class Adult(Person):
    def can_run(self):
        return True

    def need_help(self):
        return False

    def is_young(self):
        return False

    def can_vote(self):
        return True

    def can_be_married(self):
        return True

    def can_have_child(self):
        return True


class Senior(Person):
    def can_run(self):
        return False

    def need_help(self):
        return True

    def is_young(self):
        return False

    def can_vote(self):
        return True

    def can_be_married(self):
        return True

    def can_have_child(self):
        return False
