myList = [1, 2, 3, 4, 5]
while len(myList) > 0:
    num = int(input("Choose a number to delete: "))
    if num in myList:
        myList.remove(num)
        print(myList)
    elif num not in myList:
        break
