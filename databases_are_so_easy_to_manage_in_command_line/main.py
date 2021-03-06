from sys import *
from actions import *
from re import *

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

        if action_requested not in ['create',
                                    'age_average',
                                    'print_all',
                                    'export_json'] \
           and len(arguments) < 3:
            # wrong number of arguments passed
            return False

        if action_requested in ['print', 'insert', 'delete'] \
           and arguments[2] not in tables:
            # improper value passed for table
            print "Undefined table value", arguments[2]
            return False

        if action_requested in ['print_batch_by_school',
                                'print_student_by_batch',
                                'print_student_by_school',
                                'change_batch',
                                'note_average_by_student',
                                'note_average_by_school',
                                'note_average_by_batch',
                                'top_batch',
                                'top_school'] \
           and not search(r"\A\d+\Z", arguments[2]):
            # improper value passed for school, batch or student ID
            print "Invalid ID value", arguments[2]
            return False

        if action_requested == 'print_family' \
           and not search(r"\A\D+\Z", arguments[2]):
            # improper value passed for last name of student
            print "Invalid last name value", arguments[2]
            return False

        if action_requested == 'age_average' and len(arguments) > 2 \
           and not search(r"\A\d+\Z", arguments[2]):
            # improper value passed for batch ID
            print "Invalid ID value", arguments[2]
            return False

        if action_requested == 'change_batch' \
           and not search(r"\A\d+\Z", arguments[3]):
            # improper value passed for batch ID
            print "Invalid ID value", arguments[3]
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
        'change_batch': run_change_batch,
        'note_average_by_student': run_note_average_by_student,
        'note_average_by_batch': run_note_average_by_batch,
        'note_average_by_school': run_note_average_by_school,
        'top_batch': run_top_batch,
        'top_school': run_top_school,
        'export_json': run_export_json
    }

    models = { 'basemodel': BaseModel,
               'school': School,
               'batch': Batch,
               'user': User,
               'student': Student,
               'exercise': Exercise }

    if check_arguments(argv, commands.keys(), models.keys()) == True:
        # valid arguments passed; run command
        action_requested = argv[1]
        parameter_1 = (argv[2] if len(argv) > 2 else None)
        parameter_2 = (argv[3] if len(argv) > 3 else None)

        if action_requested == 'create':
            run_create(models.values())

        elif action_requested == 'insert':
            run_insert(argv)

        elif action_requested in ['print', 'delete']:
            table = models[parameter_1]
            commands[action_requested](table, argv)

        elif action_requested in ['print_batch_by_school',
                                'print_student_by_batch',
                                'print_student_by_school',
                                'print_family',
                                'age_average',
                                'note_average_by_student',
                                'note_average_by_batch',
                                'note_average_by_school']:
            commands[action_requested](parameter_1)

        elif action_requested in ['change_batch', 'top_school', 'top_batch']:
            commands[action_requested](parameter_1, parameter_2)

        elif action_requested in ['print_all', 'export_json']:
            commands[action_requested]()

    break
