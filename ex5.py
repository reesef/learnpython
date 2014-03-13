name = 'Zed A. Shaw'
age = 35 # not a lie
dog_age = age / 7.0
height = 74 # inches
weight = 180 # lbs
k_weight = 180 * 2.2
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# tricky line
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# k_weight
print "I weight %d in kilos" % k_weight

# dog age
print "I am %d years old in dog years." % dog_age
