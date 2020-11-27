Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=['1','2','3','4','5']
>>> 
>>> 
>>> l.append('6')
>>> print(l)
['1', '2', '3', '4', '5', '6']
>>> 
>>> 
>>> l.remove('2')
>>> print(l)
['1', '3', '4', '5', '6']
>>> 
>>> 
>>> print(max(l))
6
>>> print(min(l))
1
>>> 
>>> 
>>> tuple=('1','2','3','4','9','8')
>>> reversedtuples=tuple[::-1]
>>> print(reversedtuples)
('8', '9', '4', '3', '2', '1')
>>> 
>>> 
>>> tuple=('11','22','33','44')
>>> list=list(tuple)
>>> print(type(list))
<class 'list'>
>>> print(list)
['11', '22', '33', '44']
>>> 
