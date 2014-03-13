# this function is like scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this does the same thing as print_two
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this takes only one argument
def print_one(arg1):
	print "arg1: %r" % (arg1)

# no args
def print_none():
	print "I got nothin."

print_two("Filip", "Reese")
print_two_again("Filip", "Reese")
print_one("first!")
print_none()
