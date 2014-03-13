from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()

out_file = open(to_file, 'w').write(indata)

# def success:
# 	if exists(from_file) == True:
# 		print "Copyied from %s to %s" % (from_file, to_file)
#	else:
#		print "Failed to copy file"