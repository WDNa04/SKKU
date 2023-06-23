snack_type = input("snack_type: ")
quantity = int(input("quantity: "))
A_stock = 3
B_stock = 5
C_stock = 10
A_price = 1000
B_price = 2500
C_price = 3300

if snack_type == "A":
	if quantity <= A_stock:
		print(quantity * 1000)
	else:
		print("Sorry")
elif snack_type == "B":
	if quantity <= B_stock:
		print(quantity * 2500)
	else:
		print("Sorry")
elif snack_type == "C":
	if quantity <= C_stock:
		print(quantity * 3300)
	else:
		print("Sorry")

