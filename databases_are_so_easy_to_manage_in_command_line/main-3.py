import sys
import models

# if no arguments were passed (excluding the filename itself)
if len(sys.argv) == 1:
    print "Please enter an action"

# if the first argument passed is not "create", "print", "insert", or "delete"
elif sys.argv[1] not in ["create", "print", "insert", "delete"]:
    print "Undefined action " + sys.argv[1]

else:    
    if sys.argv[1] == "create":
        # execute create command

    elif sys.argv[1] == "print":
        # execute print command

    elif sys.argv[1] == "insert":
        # execute insert command
    
    elif sys.argv[1] == "delete":
        # execute print command
