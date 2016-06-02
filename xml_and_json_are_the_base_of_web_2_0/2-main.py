from car import Car

c = Car(name="Rogue", brand="Nissan", nb_doors=5)
print c
print c.get_brand()
print c.to_hash()

guillaume@production-503e7013:$ python 2-main.py
Rogue Nissan (5)
Rogue
{'nb_doors': 5, 'brand': 'Nissan', 'name': 'Rogue'}
