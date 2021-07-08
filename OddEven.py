all_x = []
odd = []
even = []

#Array size
x = int(input('Array size = '))

for i in range(x):
  i += 1
  #Creating list
  all_x.append(i)

  #Separating lists
  if i % 2 != 0:
    odd.append(i)
  else:
    even.append(i)  

print(odd)
print(even)