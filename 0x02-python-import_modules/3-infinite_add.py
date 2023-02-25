#!/usr/bin/python3
if __name__ == "__main__":
    import sys
length = len(sys.argv) -1
sum = 0
if length == 0:
    print("0")
else:
    for i in range(length):
        sum += int(sys.argv[i + 1])
    print("{}".format(sum))
