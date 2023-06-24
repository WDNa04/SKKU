students_list = []
while True:
    name = input("Input student's name: ")
    if name == "Stop":
        break
    else:
        students_list.append(name)

def lastname(name):
	last = name.split()[1]
	return len(last)

students_list.sort(key = lastname)
# This also works: students_list.sort(key = lambda x: len(x.split()[1])) 
print(students_list)
