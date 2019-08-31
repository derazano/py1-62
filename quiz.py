print('quiz1')
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
d = int(input('Enter a: '))
e = int(input('Enter b: '))
n1 = a/b
n2 = c*d
x = n1-n2+e
print(x)

print('quiz2')

u = int(input('Enter a number of initial velocity(m/s): '))
a = int(input('Enter a number of Acceleration(m/s^2): '))
s = int(input('Enter a number of Displacement(V): '))

v = ((u**2) + (2*a*s))**0.5
print("The final velocity(V) is %d m/s"%(v))
