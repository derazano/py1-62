n = int(input("input a number: "))

for i in range(1,11):
    print(n,"x",i, "=",(n*i))

print("-----------------------------")
x = 0
for i in range(0,10):
        x += i
print("sum of number 0-9 is ",x)
print("-----------------------------")

for i in range(0,7):
    if (i == 3 or i == 6):
        continue
    print(i)
print("-----------------------------")
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
print("-----------------------------")
i=0
sumn=0
while (i <= 100):
    if(i%2 == 0):
            sumn+=i
    i+=1
print(sumn)
print("-----------------------------")
s = input("Input a string: ")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)

