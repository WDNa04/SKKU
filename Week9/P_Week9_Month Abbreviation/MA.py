m = []
while True:
    month = input()
    if month == "0":
        break
    m.append(month)

i = 0
while i < len(m):
    m[i] = m[i][:3]
    i += 1

print(m)
