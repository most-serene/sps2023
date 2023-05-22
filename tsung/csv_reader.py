file = open("200UsersTimes.csv", "r")

n = 0
s = 0
for l in file:
    s += float(l.split(',')[1])
    n += 1

print(s)
print(n)
print(s/n)