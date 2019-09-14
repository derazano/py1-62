products = {"SMART WATCH": 550,"PHONE" : 1000,"PLAYSTATION": 500,"LAPTOP" : 1550,"MUSIC PLAYER" : 600,"TABLET" : 400}

price = int(input("Enter the price: "))

for p_key,value in products.items():
    if(value <= price):
        print(p_key,":" ,value)
