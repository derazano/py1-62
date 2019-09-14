def printinfo(arg1,*vartuple):
    "This prints a variable passed argument"
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)

    print(arg1)
    return;

printinfo(10)
printinfo(70 ,80 ,90, 999)
