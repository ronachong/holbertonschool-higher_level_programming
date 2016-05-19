from family import Person

p = Person(1, "Julien", [12, 24, 1980], "Male", "Blue")
p.last_name = "Dupont"
print "New person %s %s" % (p.get_first_name(), p.last_name)

# p = Person("n", "Julien", [12, 24, 1980], "Male", "Blue")
# p = Person(1, "", [12, 24, 1980], "Male", "Blue")
# p = Person(1, 0, [12, 24, 1980], "Male", "Blue")
# p = Person(1, "Julien", 12, "Male", "Blue")
# p = Person(1, "Julien", [12, 1980], "Male", "Blue")
# p = Person(1, "Julien", [13, 24, 1980], "Male", "Blue")
# p = Person(1, "Julien", [12, 32, 1980], "Male", "Blue")
# p = Person(1, "Julien", [12, 24, "foo"], "Male", "Blue")
# p = Person(1, "Julien", [12, 24, 1980], 10, "Blue")
# p = Person(1, "Julien", [12, 24, 1980], "Purple", "Blue")
# p = Person(1, "Julien", [12, 24, 1980], "Male", 10)
# p = Person(1, "Julien", [12, 24, 1980], "Male", "Cool")
