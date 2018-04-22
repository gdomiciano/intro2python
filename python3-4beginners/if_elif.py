#Operators:
# <, >, ==, !=, =>, =<

age = int(input('Enter your age: '))

if age < 10:
  #code block
  print('you are young')
elif age < 40:
  print('the fire in you is strong')
else:
  print('you are wise beyond doubt')


meaty = input('Do you eat meat? (y/n)')

if meaty == 'y':
  print('here is the meaty menu...')
else:
  print('here is the veggie menu...')
