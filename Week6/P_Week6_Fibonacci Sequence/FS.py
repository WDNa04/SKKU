N = int(input("Write the number N: "))
n1 = 0
n2 = 1
s = 1
j = 1
while j <= N:
    print(s)
    s = n1+n2
    n1 = n2
    n2 = s
    j += 1