from sys import *
from actions import *
import re

# HELPER METHODS
def check_arguments(arguments, options, tables):
    if len(arguments) < 2:
        # no action submitted: print error message
        print "Please enter an action"
        return False

    # otherwise: an action has been submitted
    action_requested = arguments[1]

    if action_requested in options:
        # action submitted is valid;
        # check if parameters to execute commands are valid;
        # (eventually - raise exceptions if not?)

        if action_requested not in ['create', 'age_average', 'print_all'] \
           and len(arguments) < 3:
            # wrong number of arguments passed
            return False

        if action_requested in ['print', 'insert', 'delete'] \
           and arguments[2] not in tables:
            # improper value passed for table
            print "Undefined table value", arguments[2]
            return False

        if action_requested in ['print_batch_by_school', 'print_student_by_batch', 'print_student_by_school', 'change_batch'] \
           and not re.search(r"\d+", arguments[2]):
            # improper value passed for school, batch or student ID
            return False

        if action_requested == 'print_family' and type(arguments[2]) != str:
            # improper value passed for last name of student
            return False

        if action_requested == 'age_average' and len(arguments) > 2 \
           and type(arguments[2]) != int:
            # improper value passed for batch ID
            return False

        if action_requested == 'change_batch' and type(arguments[3]) != int:
            # improper value passed for batch ID
            return False

        else:
            # parameters entered meets all requirements
            return True

    else:
        # action submitted does not match options: print error message
        print "Undefined action", command_key
        return False


# MAIN CODE

while True:
    commands = {
        'create': run_create,
        'print': run_print,
        'print_batch_by_school': run_print_batch_by_school,
        'print_student_by_batch': run_print_student_by_batch,
        'print_student_by_school': run_print_student_by_school,
        'print_family': run_print_family,
        'print_all': run_print_all,
        'insert': run_insert,
        'delete': run_delete,
        'age_average': run_age_average,
        'change_batch': run_change_batch
    }

    models = { 'basemodel': BaseModel,
               'school': School,
               'batch': Batch,
               'user': User,
               'student': Student }

    if check_arguments(argv, commands.keys(), models.keys()) == True:
        # valid arguments passed; and run command
        action_requested = argv[1]
        if action_requested == 'create':
            run_create(models.values())

        if action_requested == 'insert':
            run_insert(argv)

        if action_requested in ['print', 'delete']:
            table = models[argv[2]]
            commands[action_requested](table, argv)

        if action_requested in ['print_batch_by_school',
                                'print_student_by_batch',
                                'print_student_by_school']:
            commands[action_requested](argv[2])

    break
