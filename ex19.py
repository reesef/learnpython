# def our function with two args
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# print number of cheeses as set by arg
	print "You have %d cheeses!" % (cheese_count)

	# print number of crackers as set by arg
	print "You have %d boxes of crackers!" % (boxes_of_crackers)
	
	# print a some copy and leave a trailing space
	print "Thats enough for a party!"
	print "Get a blanket.\n"

# run cheese_and_crackers with args
print "We can give the function numbers directly:"
cheese_and_crackers(20, 30)

# assign some global variables
print "Or, we can give the function variables:"
amt_of_cheese = 10
amt_of_crackers = 50

# run our function with these variables
cheese_and_crackers(amt_of_cheese, amt_of_crackers)

# use math inside the args
print "Or, we can do math:"
cheese_and_crackers(5 + 35, 90 - 30)

# combine math and variables
print "And, we can also combine variables and math:"
cheese_and_crackers(amt_of_cheese + 10, amt_of_crackers - 1)
