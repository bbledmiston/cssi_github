import sys

num_lines = raw_input("how many lines?")
num_lines = int(num_lines)


for x in range(1,num_lines+1):

    num_hash = x
    num_spaces = num_lines-x



    for i in range(0, num_spaces):
        sys.stdout.write(" ")

    for i in range(0, num_hash):
        sys.stdout.write("#")

    sys.stdout.write("  ")

    for i in range(0, num_hash):
        sys.stdout.write("#")

    print("")
