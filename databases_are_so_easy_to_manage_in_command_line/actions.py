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
    elif table_key == 'exercise': record = Exercise.create(
            student=argv[3],
            subject=argv[4],
            note=argv[5])

    print "New " + table_key + ":", record

def run_delete(table, argv):
    try:
        record = table.get(id=argv[3])
        record.delete_instance()
        print "Delete:", record
    except:
        print "Nothing to delete"

def run_print_batch_by_school(school_ID):
    try:
        School.get(id=school_ID)
        for record in Batch.select().where(Batch.school==school_ID):
            print record

    except:
        print "School not found"

def run_print_student_by_batch(batch_ID):
    try:
        Batch.get(id=batch_ID)
        for record in Student.select().where(Student.batch==batch_ID):
            print record

    except: 
        print "Batch not found"
    
def run_print_student_by_school(school_ID):
    try:
        School.get(id=school_ID)
        for record in Student.select().join(Batch).where(Batch.school==school_ID):
            print record

    except:
        print "School not found"
    
def run_print_family(stu_last_name):
    try:
        Student.get(last_name=stu_last_name)
        for record in Student.select().where(Student.last_name==stu_last_name):
            print record

    except:
        print "Last name not found"

def run_age_average(batch_ID):
    if batch_ID == None:
        record = Student.select(fn.Avg(Student.age).alias('average_age')).get()

    else:
        try: Batch.get(id=batch_ID)
        except: print 'Batch not found'; return

        record = Student.select(fn.Avg(Student.age).alias('average_age')).where(
            Student.batch==batch_ID).get()

    print record.average_age

    ''' alternatively could use:
    sum = 0
    num_students = 0
    selection_pool = (Student.select() if batch_ID == None \
                     else Student.select().where(Student.batch==batch_ID))

    for record in selection_pool:
        sum += record.age
        num_students += 1
    
    average = sum/num_students
    print average
    '''

def run_change_batch(student_ID, batch_ID):
    try: student = Student.get(id=student_ID)
    except: print 'Student not found'; return

    try: batch = Batch.get(id=batch_ID)
    except: print 'Batch not found'; return

    if student.batch == batch:
        print student, "already in", batch
    else:
        print student, "has been moved to", batch
        student.batch = batch_ID
        student.save()

def run_print_all():
    for school_rec in School.select():
        print school_rec
        for batch_rec in school_rec.batches:
            print "\t", batch_rec
            for student_rec in batch_rec.students:
                print "\t\t", student_rec
                for exercise_rec in student_rec.exercises:
                    print "\t\t\t", exercise_rec
