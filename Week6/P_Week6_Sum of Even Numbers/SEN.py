num = int(input("Input a number: "))
s = 0
i = 0
while i<=num:
	if i%2==0:
		s += i
	i+=1
print(s)