listN = []
for i in range(7):
    element = int(input("Input the integer: "))
    listN.append(element)

average = sum(listN)/len(listN)
listN.sort(key= lambda x: abs(average - x))
print(listN)