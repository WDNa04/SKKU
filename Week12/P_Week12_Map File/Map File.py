wx = int(input("water x: "))
wy = int(input("water y: "))
tx = int(input("tree x: "))
ty = int(input("tree y: "))

with open("map.txt","w") as f:
	a = []
	for i in range(5):
		a.append(['O', 'O', 'O', 'O', 'O'])
	a[wy][wx]= 'W'
	a[ty][tx]= 'T'
	i = 0
	while i<5:
		line = ''
		for x in a[i]:
			line += x
		print(line)
		i+=1

with open("map.txt", "r") as f:
	lines = f.readlines()
	for line in lines:
		print(line.strip())