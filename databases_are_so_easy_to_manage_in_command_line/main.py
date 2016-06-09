import sys

# if no arguments were passed (excluding the file name itself)
if len(sys.argv) == 1:
    print "Please enter an action"

# if the first argument passed is not "create", "print", "insert", or "delete"
elif sys.argv[1] not in ["create", "print", "insert", "delete"]:
    print "Undefined action " + sys.argv[1]

# if the first argument passed IS "create", "print", "insert", or "delete"
else:
    print sys.argv[1]
