def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % (cheese_count)
	print "You have %d boxes of crackers!" % (boxes_of_crackers)
	print "Thats enough for a party!"
	print "Get a blanket.\n"

print "We can give the function numbers directly:"
cheese_and_crackers(20, 30)

print "Or, we can give the function variables:"
amt_of_cheese = 10
amt_of_crackers = 50

cheese_and_crackers(amt_of_cheese, amt_of_crackers)

print "Or, we can do math:"
cheese_and_crackers(5 + 35, 90 - 30)

print "And, we can also combine variables and math:"
cheese_and_crackers(amt_of_cheese + 10, amt_of_crackers - 1)
