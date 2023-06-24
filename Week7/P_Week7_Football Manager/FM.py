n = int(input("Input the length of roster: "))
roster = []
while len(roster) < n:
	command = input("Command: ")
	if command == 'sign':
		name = input("Name: ")
		if name in roster:
			print ("Wrong player name!")
		elif name not in roster:
			roster.append(name)
	if command == 'done':
		break
roster.sort()
print(roster)
