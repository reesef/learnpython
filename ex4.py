# Set cars variable to 100
cars = 100

# Set seats per car to 4.0
space_in_a_car = 4.0

# Set total # of drivers to 30
drivers = 30

# Set passengers to 90
passengers = 90

# Set cars not drien to cars minus drivers
cars_not_driven = cars - drivers

# Make cars driven equal to the # of drivers
cars_driven = drivers

# Set carpool capacity to cars_driven times spaces_in_a_car
carpool_capacity = cars_driven * space_in_a_car

# Set avg pass per car to the # of passengers divided by cars driven
average_passengers_per_car = passengers / cars_driven

# This block prints all the values in strings
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."