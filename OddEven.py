all_x = []
odd = []
even = []

#Array size
x = int(input('Array size = '))

#Creating list
for i in range(x):
  i += 1
  all_x.append(i)

#Separating lists
for i in all_x:
  if i % 2 != 0:
    odd.append(i)
  else:
    even.append(i)

print(odd)
print(even)