#string formatting
"""
String formatting provides a more powerful way to embed non-strings within strings.
 String formatting uses a string's format method to substitute a number of arguments in the string.
"""
nums = [4,5,6]
msg = "Numbers:{0}{1}{2}".format(nums[0],nums[1],nums[2])
print(msg)

#string formatting can also be done with named arguments
a ="{x},{y}".format(x=5,y=9)
print(a)

#string functions
"""
Python contains many useful built-in functions and methods to accomplish common tasks. 
join - joins a list of strings with another string as a separator. 
replace - replaces one substring in a string with another.
startswith and endswith - determine if there is a substring at the start and end of a string, respectively. 
To change the case of a string, you can use lower and upper.
The method split is the opposite of join, turning a string with a certain separator into a list.
"""
print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"
