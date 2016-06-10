from sys import *
import models
from peewee import *

# if no arguments were passed (excluding the filename itself)
if len(argv) == 1:
    print "Please enter an action"

elif argv[1] == "create":
    # create all tables related to models
    my_models_db.connect()
    my_models_db.create_tables([BaseModel, School, Batch, User, Student])
    # not sure of the merits of try/except clauses here

elif argv[1] == "print":
    # print data for each record in requested table
    print_table()

elif argv[1] == "insert":
    # execute insert command
    if argv[2] == "school": School.create(name=argv[3])
    if argv[2] == "batch": Batch.create(school=argv[3], name=argv[4])
    if argv[2] == "student": Student.create(batch=argv[3], age=argv[4], \
        last_name=argv[5], first_name=argv[6])
    print "New " + argv[2] + ": "
    print_table()

elif argv[1] == "delete":
    if argv[2] == "school": delete_record(School)
    if argv[2] == "batch": delete_record(Batch)
    if argv[2] == "student": delete_record(Student)
    print "Delete: " + argv[2] + " " + argv[3] # this shouldn't print if delete_record raises an exception, right?

else:
    print "Undefined action " + sys.argv[1]    
    
# HELPER METHODS
def print_table:
    if argv[2] == "basemodel": print_records(BaseModel)
    if argv[2] == "school": print_records(School)
    if argv[2] == "batch": print_records(Batch)
    if argv[2] == "user": print_records(User)
    if argv[2] == "student": print_records(Student)
        
def print_records(table):
    for record in table.select(): print record
# not sure if record will map back onto Python instance of class?
# or do I manually print each of the values from the record?        

def delete_record(table):
    try:
        table.delete(id=argv[3])
    except OperationalError:
        print "Nothing to delete"
