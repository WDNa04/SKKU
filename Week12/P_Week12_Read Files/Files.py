# Assume such file exists.

with open('data/newfile.txt', 'r') as f:
	data =f.readlines()
	for i in data:
		print(i)