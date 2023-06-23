math_score = float(input("Math score: "))
eng_score = float(input("English score: "))
if math_score >=70 and eng_score >= 70:
	print("Class A")
elif math_score >=70 and eng_score < 70:
	print("Class B")
elif math_score <70 and eng_score >= 70:
	print("Class C")
else:
	print("Class D")
	