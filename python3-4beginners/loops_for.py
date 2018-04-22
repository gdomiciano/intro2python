ninjas = ['ryu', 'crystal', 'yoshi', 'ken']

# for ninja in ninjas:
#   print(ninja)

# # loop through a section of the list
# for ninja in ninjas[1:3]:
#   print(ninja)

for ninja in ninjas:
  if ninja == 'yoshi':
    print(f'{ninja} - black belt')
  else:
    print(ninja)

#break a loop
for ninja in ninjas:
  if ninja == 'yoshi':
    print(f'{ninja} - black belt')
    break
  else:
    print(ninja)


