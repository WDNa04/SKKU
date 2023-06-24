male = input("Input the name of Male Line: ")
mare = input("Input the name of Mare Line: ")

def naming(male, mare):
	return male.split('_')[0]+'_'+mare.split('_')[1]

print(f'Name: {naming(male, mare)}')
