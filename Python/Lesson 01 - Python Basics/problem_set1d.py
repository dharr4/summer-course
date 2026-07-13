print("Welcome.")

miles_str = input("How many miles is the trip?")

miles_flt = float(miles_str)



mpg_str = input("What is your vehicles miles per gallon?")

mpg_flt = float(mpg_str)

price_gas = input("What is the current price of gas in dollars?")

price_gas_flt = float(price_gas)

#Calculate the total fuel cost and gallons needed for the trip

dist_this_trip = miles_flt / mpg_flt
dist_this_trip_flt = float(dist_this_trip)

print("--Road trip fuel estimates--")
print(f"Distance: {miles_flt}")
print(f"Fuel efficiency: {mpg_flt} per gallon.")
print(f"Gas price: {price_gas_flt} per gallon.")
print()
print(f"Gallons needed: {dist_this_trip_flt}")
print(f"Total fuel cost: {dist_this_trip_flt * price_gas_flt}")