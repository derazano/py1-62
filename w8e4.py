x = [10,20,30,40,50]
def sumNum(x):
    sm = 0
    for i in range(len(x)):
        sm += x[i]
    return sm;

print("SUM = ",sumNum(x))
