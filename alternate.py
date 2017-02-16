from profanity import profanity

file = open("url")
contents = file.read()
#The following will return 'True' or 'False', whatever suits the case.
profanity.contains_profanity(contents)
