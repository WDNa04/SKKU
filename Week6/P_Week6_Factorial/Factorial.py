n = int(input("Enter a number: "))
i = 1
s = 1
while i <= n:
    s = s * i
    i += 1
print(s)

def factorial(n):
    output = 1
    for i in range (1,n+1):
        output *= i
    return output
print(factorial(n))
