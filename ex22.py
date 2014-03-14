# Pydictionary

print 'print something'

'' use for strings and printing
"" use for string and priting

""" """ for multiline comments
# comments

+ add
- subtract
* multiply
** exponent
/ divide
% modulus returns the remainder of a division
> greater than
< less than
>= greater than or equal to
<= less than or equal to
== equals
+= # incrementer: x = x + y or x += y

= assign a variable


% for string string interpolation
%s string interpolation of strings
%d string interpolation of numbers
%r string interpolation of raw inputs

True boolean true
False boolean false

\\ backslash
\' single quote
\" double quote
\a BEL
\b backspace
\f formfeed
\n new line
\N {name}
\r carriage return
\t horizontal tab
\uxxxx 16-bit hex
\uxxxxxxxx 32-bit hex
\v vertical tab
\ooo octal value ooo
\xhh hex value hh


from sys import argv # improts argv module from sys lib
from os.path import exists # imports exists module from os.path

raw_input() # command prompt, takes args for example raw_input('> ')
int() # converts strings and numbers to integers
open() # opens files
close() # closes files
read() # reads files
truncate() # truncates files
write() # writes to file
exists() # checks if something exits (requires module)
len() # gets the lenght of a string (maybe an object too?)

def asterisk_arg(*args): # defines a funciton
	arg1, arg2 = args # defines the args of a function
	# function body

arterisk_arg() # calls this funciton

def function_name(arg1, arg2): # defins a function
	# function body
	return arg1, arg2 # return things that can be put in vars and do stuff with

function_name(x, y) # calls a function
	
def if_else(): # example of an if else statement inside a function
	if some condition == true/false:
		# do sometthing
	else:
		# do something

if_else() # calls this function