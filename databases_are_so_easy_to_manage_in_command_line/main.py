from sys import *
from models import *
# from peewee import *

    
# HELPER METHODS
def print_table():
    if argv[2] == "basemodel": print_records(BaseModel)
    elif argv[2] == "school": print_records(School)
    elif argv[2] == "batch": print_records(Batch)
    elif argv[2] == "user": print_records(User)
    elif argv[2] == "student": print_records(Student)
        
def print_records(table):
    for record in table.select(): print record
# not sure if record will map back onto Python instance of class?
# or do I manually print each of the values from the record?        

def delete_record(table):
    try:
        record = table.get(id=argv[3])
        print "Delete:", record
        record.delete_instance()
        print "Delete:", record
    except:
        print "Nothing to delete"


# if no arguments were passed (excluding the filename itself)
if len(argv) == 1:
    print "Please enter an action"

elif argv[1] == "create":
    # create all tables related to models
    my_models_db.connect()
    my_models_db.create_tables([BaseModel, School, Batch, User, Student])
    # not sure of the merits of try/except clauses here

elif argv[1] == "print":
    if len(argv) < 3: pass
    # else print data for each record in requested table
    else: print_table()

elif argv[1] == "insert":
    # execute insert command
    if argv[2] == "school": record = School.create(name=argv[3])
    elif argv[2] == "batch": record = Batch.create(school=argv[3], name=argv[4])
    elif argv[2] == "student" and len(argv) == 7:
        record = Student.create(
            batch=argv[3], \
            age=argv[4], \
            last_name=argv[5], \
            first_name=argv[6])
    elif argv[2] == "student" and len(argv) == 6:
        record = Student.create(
            batch=argv[3], \
            age=argv[4], \
            last_name=argv[5])
    print "New " + argv[2] + ":", record

elif argv[1] == "delete":
    if argv[2] == "school": delete_record(School)
    elif argv[2] == "batch": delete_record(Batch)
    elif argv[2] == "student": delete_record(Student)

else:
    print "Undefined action " + argv[1]    

