from family import Person, Baby, Teenager, Adult, Senior
from family import load_from_file, save_to_file

# new adult
a = Adult(0, "Abigail", [10, 24, 1990], "Female", "Blue")
c = Adult(1, "Carl", [7, 15, 1992], "Male", "Brown")
d = Senior(2, "Darlene", [3, 4, 1968], "Female", "Brown")

json_hash = {'a': Person.json(a), 'c': Person.json(c), 'd': Person.json(d)}
print json_hash

save_to_file(json_hash, "my_family.json")

my_family = load_from_file("my_family.json")
print "I have %d members in my family" % len(my_family)

# new baby!
b = Baby(3, "Tony", [7, 4, 2015], "Male", "Green")
b.last_name = "Foto"
my_family.append(b)

save_to_file(my_family)
