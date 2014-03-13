# import argv for command line args
from sys import argv

# set these args to script and input file
script, input_file = argv

# pass this function a file (f) and it will print the whole thing
def print_all(f):
	print f.read()

# find the beginning of the file
def rewind(f):
	f.seek(0)

# print line number and then read the line
# this function takes 2 args, line_count (a number) and a file
def print_a_line(line_count, f):
	print line_count, f.readline()

# set the current file to the second command line arg
current_file = open(input_file)

# print the entirety of the current file
print "First lets print the entire file:\n"
print_all(current_file)

# go back to the very beginning of the file
print "Now, lets rewind like a tape."
rewind(current_file)


print "Now lets print three lines:"
# set the current line to line 1
current_line = 1
# print the current_line and the first line from that file
print_a_line(current_line, current_file)

# increment current line, then print it and the line
current_line += 1
print_a_line(current_line, current_file)

# increment to the next line, then print it out
current_line += 1
print_a_line(current_line, current_file)