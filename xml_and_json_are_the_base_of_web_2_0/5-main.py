import json
from car import Car

# read file with filename 5-main.json; store in <variable>
file = open("5-main.json")
file_contents = json.loads(file.read())

# create array for brands
brands = []

# create int for cumulative no. of doors for all cars
cnb_doors = 0

# for every car hash in <variable>, call car constructor with hash as dictionary
for i in file_contents:
    car = Car(i)

    # get brand of car, number of doors
    brand = car.get_brand()
    nb_doors = car.get_nb_doors()

    # check if brand has already been accounted for in brands
    # (if not, add)
    if brand not in brands:
        brands.append(brand)

    # add number of doors from car to cnb_doors
    cnb_doors += nb_doors

# print number of different brands, print cumulative number of doors
print len(brands)
print cnb_doors

# print description of last car
last_car = Car(file_contents[-1])
print last_car
