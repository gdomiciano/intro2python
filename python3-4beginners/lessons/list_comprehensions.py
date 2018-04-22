prizes = [5, 10, 50, 100, 1000]

#conventional way:
dbl_prizes = []
for prize in prizes:
  dbl_prizes.append(prize*2)
print(dbl_prizes)

#comprehension method
dbl_prizes = [prize*2 for prize in prizes]
print(dbl_prizes)

numbers = [1,2,3,4,5,6,7,8,9,10]

#conventional way:
squared_numbers_even = []
for num in numbers:
  if (num**2) % 2 == 0:
    squared_numbers_even.append(num**2)
print(squared_numbers_even)

#comprehension method
squared_numbers_even = [num**2 for num in numbers if(num**2) % 2 == 0]
print(squared_numbers_even)
