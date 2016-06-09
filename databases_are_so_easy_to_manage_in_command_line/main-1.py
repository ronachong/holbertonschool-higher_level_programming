import sys
import models

# if no arguments were passed (excluding the filename itself)
if len(sys.argv) == 1:
    print "Please enter an action"

elif sys.argv[1] == "create":
    # execute create command

elif sys.argv[1] == "print":
    # execute print command

elif sys.argv[1] == "insert":
    # execute insert command
    
elif sys.argv[1] == "delete":
    # execute print command
    
else:
    print "Undefined action " + sys.argv[1]
