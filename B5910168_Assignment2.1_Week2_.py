import cmath
print('Assignment1')
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
d = (b**2) - (4*a*c)
ans1 = (-b-cmath.sqrt(d))/(2*a)
ans2 = (-b+cmath.sqrt(d))/(2*a)
print("The solution are" ,complex(ans1,0), "and" ,complex(ans2,0))
