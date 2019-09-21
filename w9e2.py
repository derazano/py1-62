def add_func():
    x = int(input("Enter first number: "))
    y = int(input("Enter secound number: "))
    add = x+y
    print("%s + %s = %.1f"%(x,y,add))

def sub_func():
    x = int(input("Enter first number: "))
    y = int(input("Enter secound number: "))
    sub = x-y
    print("%s - %s = %.1f"%(x,y,sub))

def mul_func():
    x = int(input("Enter first number: "))
    y = int(input("Enter secound number: "))
    mul = x*y
    print("%s - %s = %.1f"%(x,y,mul))

def div_func():
    x = int(input("Enter first number: "))
    y = int(input("Enter secound number: "))
    div = x/y
    print("%s - %s = %.1f"%(x,y,div))
def start_pro():   
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divine")
    print("Other is end of program")
    ch = input("Enter choice(1/2/3/4): ")
    if(ch == '1'):
        add_func()
    elif(ch == '2'):
        sub_func()
    elif(ch == '3'):
        mul_func()
    elif(ch == '4'):
        div_func()
    else:
        print("your enter wrong input")
        start_pro()

start_pro()
