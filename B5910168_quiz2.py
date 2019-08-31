print('quiz2')

u = int(input('Enter a number of initial velocity(m/s): '))
a = int(input('Enter a number of Acceleration(m/s^2): '))
s = int(input('Enter a number of Displacement(V): '))

v = ((u**2) + (2*a*s))**0.5
print("The final velocity(V) is %d m/s"%(v))
