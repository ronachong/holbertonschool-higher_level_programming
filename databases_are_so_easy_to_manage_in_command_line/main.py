from sys import *
from models import *


# HELPER METHODS
def run_create():
    # create all tables related to models
    my_models_db.connect()
    my_models_db.create_tables(models.values())
    # not sure of the merits of try/except clauses here

def run_print():
    # print data for each record in specified table
    for record in table.select(): print record

def run_insert():
    if table_key == "school": record = School.create(name=argv[3])
    elif table_key == "batch": record = Batch.create(school=argv[3], name=argv[4])
    elif table_key == "student" and len(argv) == 7: record = Student.create(
            batch=argv[3], \
            age=argv[4], \
            last_name=argv[5], \
            first_name=argv[6])
    elif table_key == "student" and len(argv) == 6: record = Student.create(
            batch=argv[3], \
            age=argv[4], \
            last_name=argv[5])
    print "New " + table_key + ":", record

def run_delete():
    try:
        record = table.get(id=argv[3])
        record.delete_instance()
        print "Delete:", record
    except:
        print "Nothing to delete"


# MAIN CODE
# if no arguments were passed (excluding filename): print error message
while True:
    commands = {
        'create': run_create,
        'print': run_print,
        'insert': run_insert,
        'delete': run_delete
    }

    if len(argv) < 2:
        # no action submitted: print error message
        print "Please enter an action"
    
    elif argv[1] in commands.keys():
        # action submitted matches predefined options;
        # check if conditions to execute commands are met
        command_key = argv[1]
        models = { 'basemodel': BaseModel,
               'school': School,
               'batch': Batch,
               'user': User,
               'student': Student }
        
        if len(argv) < 3 and command == 'create': commands[command_key]()
        elif len(argv) < 3: pass # wrong number of arguments for cmd
        elif argv[2] not in models.keys(): # improper value passed for table
            print "Undefined value", argv[2]
        else:
            table_key = argv[2]
            table = models[table_key]
            commands[command_key]()

    else:
        # action submitted does not match options: print error message
        print "Undefined action", command
        
    break
