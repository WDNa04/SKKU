grades = []
i = 1
while i <=5:
	grade = int(input("Enter the grade: "))
	grades.append(grade)
	i+=1
grades.remove(min(grades))
grades.remove(max(grades))

average = sum(grades) / len(grades)
print("Average grade: {:.2f}".format(average))