Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> string = "a-zA-Z0-9"
>>> if re.findall(r'/w',string):
	print("the string contains a set of char")
else:
	print("the string does not contains a set of char")

	
the string does not contains a set of char
>>> 
>>> 
>>> import re
>>> pattern=re.compile('a.?b')
>>> match='aaabcd'
>>> if re.search(pattern,match):
	print("found a match")
else:
	print("match not found")

	
found a match
>>> 
>>> 
>>> import re
>>> test_number = "internship python program"
>>> res = len(re.findall(r'/w+',test_number))
>>> print("check the number at the end of the word is:"+str(res))
check the number at the end of the word is:0
>>> 
>>> 
>>> import re
>>> results= re.finditer(r"([0-9]{1,3})","exercises number 1,12,13 and 260 are important")
>>> print("number of length 1 to 3")
number of length 1 to 3
>>> 
>>> for n in results:
	print(n.group(0))

	
1
12
13
260
>>> 
>>> 
>>> import re
>>> def match(text):
	pattern = '[A-Z]+$'
	if re.search(pattern,text):
		return('match')
	else:
		return('match not found')

	
>>> print(match("ABCDEF"))
match
>>> print(match("GEEKS"))
match
>>> 