money = int(input('Enter your money: '))
tax = 0.0
if (money > 100000):
    tax = (money*25)/100
elif(money > 50000):
    tax = (money*15)/100
elif(money > 15000):
    tax = (money*10)/100
else:
    print("u don't have taz")
salary = money-tax
print("รายได้สุทธิ",salary,"ภาษี",tax)
