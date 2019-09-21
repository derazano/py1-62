def append_line():
    f = open("new.txt",'a')
    for i in range(5):
        f.write("Appended line %d\n"%(i+1))
    f.close()


append_line()
