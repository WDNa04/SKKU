snack = int(input("Snack: "))
ice_cream = int(input("Ice Cream: "))
juice = int(input("Juice: "))

total = snack*1200+ice_cream*900+juice*1900
if total >= 10000:
	print(int(total*0.9))
else:
	print(total)