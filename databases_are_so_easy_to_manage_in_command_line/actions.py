from models import *

def run_create(models):
    # create all tables related to models
    my_models_db.connect()
    my_models_db.create_tables(models)
    # not sure of the merits of try/except clauses here

def run_print(table, argv):
    # print data for each record in specified table
    for record in table.select(): print record

def run_insert(argv):
    table_key = argv[2]
    if table_key == "school": record = School.create(name=argv[3])
    elif table_key == "batch": record = Batch.create(school=argv[3], name=argv[4])
    elif table_key == "student" and len(argv) == 7: record = Student.create(
            batch=argv[3],
            age=argv[4],
            last_name=argv[5],
            first_name=argv[6])
    elif table_key == "student" and len(argv) == 6: record = Student.create(
            batch=argv[3],
            age=argv[4],
            last_name=argv[5])

    print "New " + table_key + ":", record

def run_delete(table, argv):
    try:
        record = table.get(id=argv[3])
        record.delete_instance()
        print "Delete:", record
    except:
        print "Nothing to delete"

def run_print_batch_by_school(school_ID):
    n = 0
    for record in Batch.select().where(Batch.school==school_ID):
        print record
        n += 1
    if n == 0: print "School not found"

def run_print_student_by_batch(batch_ID):
    n = 0
    for record in Student.select().where(Student.batch==batch_ID):
        print record
        n += 1
    if n == 0: print "Batch not found"

def run_print_student_by_school(school_ID):
    n = 0
    for record in Student.select().join(Batch).where(Batch.school==school_ID):
        print record
        n += 1
    if n == 0: print "School not found"

def run_print_family():
    pass

def run_age_average():
    pass

def run_change_batch():
    pass

def run_print_all():
    pass
