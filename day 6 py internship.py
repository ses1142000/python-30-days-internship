Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list=[2,4,6,8,0]
>>> 
>>> for i in list:
	print(i,i+2)

	
2 4
4 6
6 8
8 10
0 2
>>> 
>>> 
>>> for i in range(5,0,-1):
	for j in range(i,0,-1):
		print(j,end="")

		
543214321321211
>>> 
>>> 
>>> x,y=0,1
>>> 
>>> while y<50:
	print(y)
	x,y = y,x+y

	
1
1
2
3
5
8
13
21
34
>>> 
>>> 
>>> 
>>> num=int(input("enter a number:"))
enter a number:100
>>> sum=0
>>> temp=num
>>> while temp>0:
	digit=temp%10
	sum+=digit**3
	temp//=10
	
>>> if num==sum:
	print(num,"it is an armstrong number")
else:
	print(num,"it is not an armstrong number")

	
110 it is not an armstrong number
>>> 
>>> 
>>> num=int (input("display the multiplication table of :"))
display the multiplication table of :9
>>> for i in range(1,11):
	print(num,'x',i,'=',num*i)

	
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
>>> 
>>> 
>>> num=int (input("enter a number"))
enter a number13
>>> if num>0:
	print("{0} is a positive number".format(num))
else:
	print("{0} is a negative number".format(num))

	
13 is a positive number
>>> 
>>> 
>>> days=7665
>>> age=days/365
>>> print("age of the person is:")
age of the person is:
>>> print(age)
21.0
>>> 
>>> 
>>> import math
>>> a=math.pi/6
>>> print("the value of the sin of pi/6:",end="")
the value of the sin of pi/6:
>>> print(math.sin(a))
0.49999999999999994
>>> print(math.cos(a))
0.8660254037844387
>>> print(math.tan(a))
0.5773502691896257
>>> 
>>> 
>>> print("calculator")
calculator
>>> print("1.add")
1.add
>>> print("2.subract")
2.subract
>>> print("3.multiply")
3.multiply
>>> print("4.divide")
4.divide
>>> choice=int(input("enter choice(1-4):"))
enter choice(1-4):3

>>> if choice==1:
	a=int(input("enter A:"))
	b=int(input("enter B:"))
	c=a+b
	print("sum=",c)
elif choice==2:
	a=int(input("enter A:"))
	b=int(input("enter B:"))
	c=a-b
	print("difference =",c)
elif choice==3:
	a=int(input("enter A:"))
	b=int(input("enter B:"))
	c=a*b
	print("product =",c)
elif choice==4:
	a=int(input("enter A:"))
	b=int(input("enter B:"))
	c=a/b
	print("quotient =",c)

	
enter A:10
enter B:50
product = 500
>>> 
