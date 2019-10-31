# reading
a_prev_reading = int(input("Enter A Previous months reading: "))
b_prev_reading = int(input("Enter B Previous months reading: "))
c_prev_reading = int(input("Enter C Previous months reading: "))
a_reading = int(input("Enter A current Months reading: "))
b_reading = int(input("Enter B current Months reading: "))
c_reading = int(input("Enter C current Months reading: "))
namelist = ["Biranchi", "SBI", "Tata", "pradhan"]
Total_reading = int(input("Enter this months reading: "))
Total_price = int(input("Total price for the month: "))

# Price
a_reading_actual=a_reading-a_prev_reading
b_reading_actual=b_reading-b_prev_reading
c_reading_actual=c_reading-c_prev_reading
owners_actual_reading = Total_reading - (a_reading_actual+b_reading_actual+c_reading_actual)
per_unit_price = Total_price/Total_reading
a_price = a_reading_actual*per_unit_price
b_price = b_reading_actual*per_unit_price
c_price = c_reading_actual*per_unit_price
tenants_price = a_price+b_price+c_price
our_price = Total_price-tenants_price
price_list = [a_price, b_price, c_price, our_price]
readlist = [a_reading_actual, b_reading_actual, c_reading_actual, owners_actual_reading]
print('The per unit price is ₹{0}'.format(per_unit_price))
for (name, read, price) in zip(namelist, readlist, price_list):
    print("The price for {0} with reading of {1} units is ₹{2}".format(name, read, price))
