a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
def check_a(a,b):
    if (a>0):
        return a+b;
    if(a==0):
        return 0;
    if(a<0):
        return a*10,b;

print("check_a(%s)"%(a))
print(check_a(a,b))
print("check_a(%s)"%(a+1))
print(check_a(0,0))
print("check_a(10)")
print(check_a(a,b))
print("check_a(-50)")
print(check_a(-50,-5))

