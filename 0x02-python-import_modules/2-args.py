#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    length = len(sys.argv) - 1
    if length == 0:
        print("{} arguments.".format(length))
    elif length  == 1:
        print("{} argument:".format(length))
    else:
        print("{} arguments:".format(length))
    for index in range(length):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))
