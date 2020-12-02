	# <QUESTION 1>

	# Given a string, return the boolean True if it ends in "py", and False if not. Ignore Case.

	# <EXAMPLES>

	# endsDev("ilovepy") → True
	# endsDev("welovepy") → True
	# endsDev("welovepyforreal") → False
	# endsDev("pyiscool") → False

	# <HINT>

	# What was the name of the function we have seen which changes the case of a string?  Use your CLI to access the Python documentation and get help(str).
    
def endsPy(input):
	word = input.lower()
	if word[-2:] == "py":
		is_true = True
	else:
		is_true = False
	return print(is_true)

endsPy("ilovepy")
endsPy("welovepy") 
endsPy("welovepyforreal")
endsPy("pyiscool") 
