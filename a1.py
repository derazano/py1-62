n = int(input("input a number: "))
sumpos = 0
sumneg = 0
i = 1
for i in range(n+1):
    if(i%2 ==0):
        sumpos +=i
    elif(i%2 == 1):
        sumneg -=i
        
print("The positive summation is ",sumpos)
print("The positive summation is ",sumneg)
