def a_func():
    a = int(input("Enrer first number: "))
    b = int(input("Enter secound number: "))
    e = (a**2) - (b**2)
    print("%d^2 - %d^2 = %d"%(a,b,e))
    ch = input("Enter choice(A/B): ")
    if(ch in['A','a']):
        a_func()
    if(ch in ['B','b']):
        b_func()

def b_func():
    c = int(input("Enrer first number: "))
    d = int(input("Enter secound number: "))
    f = (c+d)**2
    print("(%d + %d)^2 = %d "%(c,d,f))
    ch = input("Enter choice(A/B): ")
    if(ch in['A','a']):
        a_func()
    if(ch in ['B','b']):
        b_func()

print("Select operation.")
print("A. Different of squares: a^2 - b^2")
print("B. Perfect square: (a+b)^2")
ch = input("Enter choice(A/B): ")
if(ch in['A','a']):
        a_func()
if(ch in ['B','b']):
        b_func()

print("Program Successs")
