import random
seed = int(input())
random.seed(seed)

b = []
for i in range(3):
	a = random.randint(0,9)
	b.append(a)

if b[0]==b[1]==b[2]==7:
	print('JACKPOT')
elif b[0]==b[1]==b[2]!=7:
	print('LUCKY')
else:
	print('LOST')
