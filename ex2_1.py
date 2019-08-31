import math
num1 = float(input('Enter first number  is: '))
num2 = float(input('Enter second number is: '))
Sum = sum([num1,num2])
print(num1)
print(num2)
print(Sum)
print ("The sum of %.1f and %.1f is %.1f" %(num1,num2,Sum))
#SquareRoot
in_sqr = int(input("Enter squreroot value: "))
sqr = (math.sqrt(in_sqr))
print('The square root of %.3f is %.3f' %(in_sqr,sqr))
# Triangle
Tri1 = int(input('Number 1 is: '))
Tri2 = int(input('Number 2 is: '))
Tri3 = int(input('Number 3 is: '))
S = (Tri1+Tri2+Tri3)/2
n = S*(S-Tri1)*(S-Tri2)*(S-Tri3)
area = (math.sqrt(n))
print('The area of Triangle is %.2f' %(area))
