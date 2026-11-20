matrix = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

i = 0
for row in matrix:
   row[i] = 1
   i += 1

for row in matrix:
   for element in row:
      print(element, end=" ")
   print()
   

