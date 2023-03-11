#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0
    for index, el in enumerate(sys.argv):
        sum += int(sys.argv[index + 1])
    print("{}".format(sum))
