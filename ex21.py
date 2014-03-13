def add(a,b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d"  % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Now lets do math with just functions!"

age = add(5, 30)
height = subtract(10, 40)
weight = multiply(30, 70)
iq = divide(80, 10)

print "Age: %d, Height: %d, Weight: %d, iq: %d" % (age, height, weight, iq)

# For extra credit
print "Here is a puzzle:"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Now, do it by hand!"

# This 'unpacks that function'
def what(a, b, c, d):
	print "Now this should be the same:"
	return a + b - c * d / 2

same = what(age, height, weight, iq)
print same