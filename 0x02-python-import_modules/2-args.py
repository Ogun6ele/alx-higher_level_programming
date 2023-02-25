#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    length = len(sys.argv)
    if length == 1:
        print("{} arguments.".format(length - 1))
    elif length  == 2:
        print("{} argument:".format(length - 1))
    else:
        print("{} arguments:".format(length - 1))
    for x in range(length):
        print("{}: {}".format(x, sys.argv[x]))
