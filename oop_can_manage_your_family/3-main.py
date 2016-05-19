from family import Person, Baby, Teenager, Adult, Senior
from family import load_from_file, save_to_file

# new adult
a = Adult(0, "Abigail", [10, 24, 1990], "Female", "Blue")
c = Adult(1, "Carl", [7, 15, 1992], "Male", "Brown")
d = Senior(2, "Darlene", [3, 4, 1968], "Female", "Brown")

json_list = []
json_list.append(Person.json(a))
json_list.append(Person.json(c))
json_list.append(Person.json(d))
print json_list

save_to_file(json_list, "my_family.json")

my_family = load_from_file("my_family.json")
print "I have %d members in my family" % len(my_family)

e = Adult(0, "foo", [1, 1, 1], "Female", "Blue")
print my_family[1]
e.load_from_json(my_family[1])
#name = Person.get_id(e)
#print name

# new baby!
b = Baby(3, "Tony", [7, 4, 2015], "Male", "Green")
b.last_name = "Foto"
my_family.append(Person.json(b))

save_to_file(my_family, "my_family.json")
