N = int(input("N = "))
s = 0
while s<N:
	n = int(input("Number ="))
	s += n
	if s == N:
		print("You won!!")
	elif s>N:
		print("Game Over!")

