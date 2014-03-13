# Import argv module 
from sys import argv

# Define command line variables with argv
script, filename = argv

# Open the sample file and make a "file object"
txt = open(filename)

# Print the name of the file
print "Here's your file %r:" % filename
# Read the file's content
print txt.read()
txt.close()

# Prompt user to give the script a filename
print "Type the filename again:"
file_again = raw_input('> ')

# Open the file and make a new "file object"
txt_again = open(file_again)
# Print the the contents of the file
print txt_again.read()
txt_again.close()