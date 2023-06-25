# Assume such files already exist.

file_name = input()
PATH = 'data/' + file_name + '.txt'
with open(PATH,'r') as f:
	data = f.readlines()
	b=0
	for i in data:
		a = i.replace("\n","")
		if a != file_name:
			b+=1
	print(b)
