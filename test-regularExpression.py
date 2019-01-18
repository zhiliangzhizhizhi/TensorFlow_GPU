# this regular expression contains no special symbols
# it won't match anything except 'cat'
"cat"

# a . stands for any single character (except the newline, by default)
# this will match 'cat', 'cbt', 'c3t', 'c!t' ...
# "c.t"

# a * repeats the previous character 0 or more times
# it can be used after a normal character, or a special symbol like .
# this will match 'ct', 'cat', 'caat', 'caaaaaaaaat' ...
# "ca*t"
# this will match 'sc', 'sac', 'sic', 'supercalifragilistic' ...
# "s.*c"

# + is like *, but the character must occur at least once
# there must be at least one 'a'
# "ca+t"

# more generally, we can use curly brackets {} to specify any number of repeats
# or a minimum and maximum
# this will match any five-letter word which starts with 'c' and ends with 't'
# "c.{3}t"
# this will match any five-, six-, or seven-letter word ...
# "c.{3,5}t"

# One of the uses for ? is matching the previous character zero or one times
# this will match 'http' or 'https'
# "https?"

# square brackets [] define a set of allowed values for a character
# they can contain normal characters, or ranges
# if ^ is the first character in the brackets, it *negates* the contents
# the character between 'c' and 't' must be a vowel
# "c[aeiou]t"
# this matches any character that *isn't* a vowel, three times
# "[^aeiou]{3}"
# This matches an uppercase UCT student number
# "[B-DF-HJ-NP-TV-Z]{3}[A-Z]{3}[0-9]{3}"

# we use \ to escape any special regular expression character
# this would match 'c*t'
# r"c\*t"
# note that we have used a raw string, so that we can write a literal backslash

# there are also some shorthand symbols for certain allowed subsets of characters:
# \d matches any digit
# \s matches any whitespace character, like space, tab or newline
# \w matches alphanumeric characters -- letters, digits or the underscore
# \D, \S and \W are the opposites of \d, \s and \w

# we can use round brackets () to *capture* portions of the pattern
# this is useful if we want to search and replace
# we can retrieve the contents of the capture in the replace step
# this will capture whatever would be matched by .*
# "c(.*)t"

# ^ and $ denote the beginning or end of a string
# this will match a string which starts with 'c' and ends in 't'
# "^c.*t$"

# | means "or" -- it lets us choose between multiple options.
# "cat|dog"

#refer to http://python-textbok.readthedocs.io/en/1.0/Useful_Libraries.html

import re

# match and search are quite similar
print(re.match("c.*t", "cravat")) # this will match
print(re.match("c.*t", "I have a cravat")) # this won't
print(re.search("c.*t", "I have a cravat")) # this will

# We can use a static string as a replacement...
print(re.sub("lamb", "squirrel", "Mary had a little lamb."))
# Or we can capture groups, and substitute their contents back in.
print(re.sub("(.*) (BITES) (.*)", r"\3 \2 \1", "DOG BITES MAN"))
# count is a keyword parameter which we can use to limit replacements
print(re.sub("a", "b", "aaaaaaaaaa"))
print(re.sub("a", "b", "aaaaaaaaaa", count=1))

# Here's a closer look at a match object.
my_match = re.match("(.*) (BITES) (.*)", "DOG BITES MAN")
print(my_match.groups())
print(my_match.group(1))

# We can name groups.
my_match = re.match("(?P<subject>.*) (?P<verb>BITES) (?P<object>.*)", "DOG BITES MAN")
print(my_match.group("subject"))
print(my_match.groupdict())
# We can still access named groups by their positions.
print(my_match.group(1))

# Sometimes we want to find all the matches in a string.
print(re.findall("[^ ]+@[^ ]+", "Bob <bob@example.com>, Jane <jane.doe@example.com>"))

# Sometimes we want to split a string.
print(re.split(", *", "one,two,  three, four"))

# We can compile a regular expression to an object
my_regex = re.compile("(.*) (BITES) (.*)")
# now we can use it in a very similar way to the module
print(my_regex.sub(r"\3 \2 \1", "DOG BITES MAN"))

# this is going to match everything between the first and last '"'
# but that's not what we want!
print(re.findall('".*"', '"one" "two" "three" "four"'))

# This is a common trick
print(re.findall('"[^"]*"', '"one" "two" "three" "four"'))

# We can also use ? after * or other expressions to make them *not greedy*
print(re.findall('".*?"', '"one" "two" "three" "four"'))