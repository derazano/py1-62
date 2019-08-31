import cmath
print('Assignment1')
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print("The solution are" ,complex(sol1,0), "and" ,complex(sol2,0))

print("**************************************")
print("Assignment2")
x = int(input('Enter x: '))
y = int(input('Enter y: '))
x +=y
y = x - y
print("%The value of x after swapping: " ,x)
print("%The value of x after swapping: " ,y)
print("**************************************")
print("Assignment3")
km = float(input("Enter your distance Kilometers: "))
mi = km*0.621371
print("%.3f Kilometers is equal to %.3f miles" %(km,mi))
