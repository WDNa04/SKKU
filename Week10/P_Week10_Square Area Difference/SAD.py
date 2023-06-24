a = int(input("Input the length of side square A: "))
b = int(input("Input the length of side square B: "))

def calculate_square_area_difference(a, b):
	return abs(a**2-b**2)

print(calculate_square_area_difference(a, b))
