f = open("mytestappend.txt",'w')

for i in range(10):
    f.write("This is line %d\n"%(i+1))
f.close()
