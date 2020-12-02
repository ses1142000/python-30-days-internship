Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = lambda x,y :x*y
>>> print(s(10,15))
150
>>> 
>>> 
>>> from functools import reduce
>>> fib = lambda n: reduce (lambda x,_: x+[x[-1]+x[-2]],
			range(n-2),[0,1])
>>> print(fib(5))
[0, 1, 1, 2, 3]
>>> 
>>> 
>>> nums=[1,3,5,7,9]
>>> n=2
>>> print("original:",nums)
original: [1, 3, 5, 7, 9]
>>> print("given number:",n)
given number: 2
>>> filtered_numbers=list(map(lambda number:number*n,nums))
>>> print("result:")
result:
>>> print(''.join(map(str,filtered_numbers)))
26101418
>>> 
>>> nums= [9,27,18,63,45,79,100,47,109]
>>> result= list(filter(lambda x: (x%9==0), nums))
>>> print("number divisible by 9 is :",result)
number divisible by 9 is : [9, 27, 18, 63, 45]
>>> 
>>> 
>>> numm=[1,2,3,4,5,6,7,8,9,10]
>>> odd = len(list(filter(lambda x: (x%2 !=0), numm)))
>>> even = len(list(filter(lambda x: (x%2 ==0), numm)))
>>> print("number of even numbers :", even)
number of even numbers : 5
>>> print("number of odd numbers :", odd)
number of odd numbers : 5
>>> 
>>> 
