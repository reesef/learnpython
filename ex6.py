# Set x to a string with a number string interpolation
x = "There are %d types of people." % 10

# set var binary to str binary
binary = "binary"

# set var do_not to don't
do_not = "don't"

# Make y a string with interpolated variables
y = "Those who know %s and those who %s." % (binary, do_not)

# print var x
print x

# print var y
print y

# print some more strings iwth variables
print "I said: %r" % x
print "I also said: '%s'." % y

# Set hilarious to boolean false
hilarious = False

# Set joke_evaluation to a string with %r var interpolation (for a binary)
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# Use + to concatentate strings
print w + e