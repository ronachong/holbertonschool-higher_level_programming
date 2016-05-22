from family import Person, Baby, Teenager, Adult, Senior
from family import load_from_file, save_to_file

# new adult
a = Adult(0, "Abigail", [10, 24, 1990], "Female", "Blue")
c = Adult(1, "Carl", [7, 15, 1992], "Male", "Brown")
d = Senior(2, "Darlene", [3, 4, 1968], "Female", "Brown")

list_of_instances = [a, c, d]
save_to_file(list_of_instances, "my_family.json")

my_family = load_from_file("my_family.json")
print "I have %d members in my family" % len(my_family)
print my_family

# new baby!
b = Baby(3, "Tony", [7, 4, 2015], "Male", "Green")
b.last_name = "Foto"
my_family.append(b)
print my_family

save_to_file(my_family, "my_family.json")
