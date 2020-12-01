Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 30/0
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    30/0
ZeroDivisionError: division by zero
>>> try:
	30/0
except:
	print("it is an exception")

	
it is an exception
>>> 
>>> 
>>> print "hi"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hi")?
>>> 
>>> 
>>> import usermodule1
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    import usermodule1
ModuleNotFoundError: No module named 'usermodule1'
>>> 
>>> 
>>> print("1.add")
1.add
>>> print("2.subract")
2.subract
>>> print("3.multiplication")
3.multiplication
>>> print("4.divide")
4.divide
>>> 
>>> def addition(n1,n2):
	try:
		result=n1+n2
		print(result)
	except exception as e:
		print(e)

		
>>> addition(6,8)
14
>>> def subract(n1,n2):
	try:
		result=n1-n2
		print(result)
	except exception as e:
		print(e)

		
>>> subract(20,22)
-2
>>> def multiply(n1,n2):
	try:
		result=n1*n2
		print(result)
	except exception as e:
		print(e)

		
>>> multiply(2,4)
8
>>> def divide(n1,n2):
	try:
		result=n1/n2
		print(result)
	except exception as e:
		print(e)

		
>>> divide(4,8)
0.5
>>> 
>>> 
>>> try:
	print(c)
except NameError:
	print("c is not defined")
except:
	print("something went wrong")

	
c is not defined
>>> try:
	a=3
	b='8'
	print(a+b)
except TypeError:
	print("operation is not supported")
except:
	print("out of try except blocks")

	
operation is not supported
>>> try:
	a=20
	b=0
	print(a/b)
except ZeroDivisionError:
	print("error by zero division")
except:
	print("out of try except blocks")

	
error by zero division
>>> 
>>> 
>>> #when codes are not present try except scenario is not required
>>> 
>>> 
>>> try:
	x=int(input("enter first value"))
	y=int(input("enter second value"))
	z=x+y
except:
	print("error")

	
enter first value2
enter second value4
>>> 
>>> print(z)
6
>>> 
