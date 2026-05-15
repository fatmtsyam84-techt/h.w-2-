cof_price=25
cof_count=2
cake_price=40
cake_count=1
water_price=10
water_count=3
total=cof_count*cof_price + cake_price* cake_count + water_count* water_price
print(total)
print(total > 100)
print(total == 120)
cof_price += 5
total=cof_count*cof_price + cake_price* cake_count + water_count* water_price
print(total)
