def getSum(q1,q2,q3):
    sum1 = q1+q2+q3
    return sum1
def getAvg(q1,q2,q3):
    avg = (q1+q2+q3)/3
    return avg

q1 = int(input("Score Q1: "))
q2 = int(input("Score Q2: "))
q3 = int(input("Score Q3: "))

print("Summation of q1 q2 q3 = ",getSum(q1,q2,q3))
print("Average of q1 q2 q3 = ",getAvg(q1,q2,q3))
