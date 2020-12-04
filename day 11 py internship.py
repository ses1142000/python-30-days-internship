Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1=[21,22,23,24]
>>> list2=['w','x','y','z']
>>> def merge(list1,list2):
	merged_list = tuple(zip(list1,list2))
	return merged_list

>>> print(merge(list1,list2))
((21, 'w'), (22, 'x'), (23, 'y'), (24, 'z'))
>>> 
>>> 
>>> list1=[1,2,3,4]
>>> list2=[11,12,13,14]
>>> list(zip(list1,list2))
[(1, 11), (2, 12), (3, 13), (4, 14)]
>>> tuple(zip(list1,list2))
((1, 11), (2, 12), (3, 13), (4, 14))
>>> 
>>> 
>>> list=[9,5,4,1,6,3,8,2,7]
>>> x=sorted(list)
>>> print("sort the list in ascending order:",x)
sort the list in ascending order: [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> 
>>> list=[9,5,4,1,6,3,8,2,7]
>>> def even_numbers(num):
	if(num%2 == 0):
		return True
	else:
		return False

	
>>> evenNo=filter(even_numbers,list)
>>> print("even numbers:")
even numbers:
>>> for num in evenNo:
	print(num)

	
4
6
8
2
>>> 
>>> 
>>> def odd_numbers(nums):
	if(nums%2==1):
		return True
	else:
		return False

	
>>> oddNo=filter(odd_numbers,list)
>>> for nums in oddNo:
	print(nums)

	
9
5
1
3
7
>>>
>>>
>>>
