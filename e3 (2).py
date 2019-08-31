number = [1,2,3,4,5,6,7,8,9]
countodd=0
counteven=0
for i in range(len(number)):
    if(number[i]%2==0):
        counteven +=1
    elif(number[i]%2==1):
        countodd +=1
    else:
        print("don't match in condiion")

print("Count thw odd and even number in the list of",number)
print("Number of even number: ",counteven)
print("Number of odd number: ",countodd)
