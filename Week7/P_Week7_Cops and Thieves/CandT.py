job_list = []

while len(job_list) < 5:
	occupation = input("Input a occupation: ")
	job_list.append(occupation)
if 'thief' in job_list:
	if 'cop' in job_list:
		print("busted")
	else:
		print('thief!')
else:
	print('peace')
