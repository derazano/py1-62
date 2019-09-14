n = input("enter your name: ")
d = input("Enter  your ID: ")


def maname(n,d):
    print("Ore no namai ha ga %s and ma id is %s"%(n,d))

maname(n,d)

def trian():
    for x in range(1,10):
        print('*'*x)
    for x in range(1,x):
        print('*'*x)
       

print("start Draw Triangle")
trian()
print("Draw Triangle Complete")
