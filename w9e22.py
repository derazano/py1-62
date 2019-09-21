import csv
f1 = open("sameple.csv",'r')

data = csv.reader(f1)

for s in data:
    print(s)


data1 = f1.read()
print(data1)

f1.close()


data1 = f1.read()
print(data1)
