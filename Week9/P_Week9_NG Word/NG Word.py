ng_list = [['Despair','Hope'],
           ['Sadness','Happiness'],
           ['Distrust','Trust'],['Rage','Peace']]
sentence = input("Input a sentence: ")
for i in ng_list:
	if i[0] in sentence:
		sentence = sentence.replace(i[0], i[1])
print(sentence)