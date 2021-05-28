all = []
odd = []
even = []

#Creating list
for i in range(25):
  i += 1
  all.append(i)

#Separating lists
for i in all:
  if i % 2 != 0:
    odd.append(i)
  else:
    even.append(i)

print(odd)
print(even)