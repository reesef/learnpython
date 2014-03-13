from sys import argv

# script, first, second, third = argv

# print "Then script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third


script_name, user_name = argv

print "This script is called:", script_name
print "The user's name is:", user_name

user_age = int(raw_input('What is your age? '))
print "You can play, your age is %d" % user_age