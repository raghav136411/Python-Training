#Write a program check_args.py that gets two command line arguments and checks that the first represents a valid int
# number and that the second represents a valid float number . Add the exception whereever necessary

import sys
args=sys.argv[1:]

try:
    args[0]=int(args[0])
    print("First arguement is an integer")
except ValueError:
    print("First arguement isn't an integer")

try:
    args[1]=float(args[1])
    print("Second arguement is a float")
except ValueError:
    print("Second arguement isn't a float")

