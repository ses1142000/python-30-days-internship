Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> keys=['name','age','role']
>>> values=['sharon','20','intern']
>>> myDict=dict(zip(keys,values))
>>> print(myDict)
{'name': 'sharon', 'age': '20', 'role': 'intern'}
>>> 
>>> 
>>> dict1={'a':1,'b':2}
>>> dict2={'c':3,'d':4}
>>> dict=dict1.copy()
>>> dict.update(dict2)
>>> print(dict)
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> 
>>> 
>>> dict.pop('a')
1
>>> print(dict)
{'b': 2, 'c': 3, 'd': 4}
>>>
>>> 
>>> set1={'1','2','3','4','5','6'}
>>> set2={'7','8','9','1','2','4'}
>>> print(set2.intersection(set1))
{'1', '2', '4'}
>>> 
>>> 
>>> set={'1','2','3','4','5','6'}
>>> print(len(set))
6
>>> 
