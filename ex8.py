# Set var formatter to 4 raw replacements
formatter = "%r %r %r %r"

# interpolate some ints into formatter
print formatter % (1, 2, 3, 4)

# put some strings in
print formatter % ("one", "two", "three", "four")

# put some booleans in
print formatter % (True, False, False, True)

# reproduce formatter exactly
print formatter % (formatter, formatter, formatter, formatter)

# put some other strings in
print formatter % (
	"I had this thing",
	"That you could tye up right.",
	"But it didn't sing",
	"So I said goodnight."
)