Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list=[13,54,75]
>>> import usermodule
>>> print ("list=",usermodule.list)
list= [13, 54, 75]
>>> list.append(98)
>>> print(list)
[13, 54, 75, 98]
>>> 
>>> 
>>> import pandas as pa
>>> import numpy as nu
>>> import sys
>>> sys._stdout_=sys.stdout
>>> fruit=nu.array(['pears','mango','kiwi'])
>>> series=pa.series(fruit)
    series=pa.series(fruit)
    print(series)
 0 pears
 1 mango
 2 kiwi
>>> 
>>> 
>>> import random
>>> print("random integer is :",random.randint(1,100))
random integer is : 42
>>> 
>>> 
>>> import sys
>>> sys.path
['', 'C:\\Users\\sharo\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\idlelib', 'C:\\Users\\sharo\\AppData\\Local\\Programs\\Python\\Python39', 'C:\\Users\\sharo\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip', 'C:\\Users\\sharo\\AppData\\Local\\Programs\\Python\\Python39\\DLLs', 'C:\\Users\\sharo\\AppData\\Local\\Programs\\Python\\Python39\\lib', 'C:\\Users\\sharo\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages']
>>> 
>>> 
>>> 
>>> 
