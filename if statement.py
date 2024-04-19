house_price = 10**6
good_Credit = False
if good_Credit:
    price = house_price + (house_price * (10/100))
else:
    price = house_price + house_price * (20 / 100)
print(f"price with down payment is ${price}")
