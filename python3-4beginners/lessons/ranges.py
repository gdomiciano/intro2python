#range creates a list of numbers (in order) not inclusive
for n in range(5):
  print(n)

#define the start and end points of the list values, when the start is inclusive and the end is non inclusive
for n in range(3, 10):
  print(n)

#third argument defines the step, in this case the numbers will be generate 4 in 4
for n in range(0, 20, 4):
  print(n)

burgers = ['beef', 'chicken', 'pork', 'veggie', 'supreme', 'double']

#define a range from variable
for n in range(len(burgers)):
  print(n, burgers[n])

# creates a reverse loop in range (negative for), where the first parameter is the last item index, the second is the last item(it should be 0, however this parameter is non inclusive, so we use -1 to actually read the 0, since we are not woring with index 5 as last index), and the third one defines the pace that is negative, due to is reading the array in backwards.
for n in range(len(burgers) - 1, -1, -1):
  print(n, burgers[n])


