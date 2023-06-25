# Assume such file exists.

path = input()

with open(path, 'r') as f:
	data = f.readlines()
	for i in data:
		print(i.split()[0]+str(":"), i.split()[1])