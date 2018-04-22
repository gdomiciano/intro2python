grades = ['A', 'B', 'F', 'C', 'F', 'A']

def remove_fails(grade):
  return grade != 'F'

#filter method
filtered_grades = list(filter(remove_fails, grades))
print(filtered_grades)

#for method
filtered_grades = []
for grade in grades:
  if remove_fails(grade):
    filtered_grades.append(grade)
print(filtered_grades)

#list comprehension method
filtered_grades = [grade for grade in grades if grade != 'F']
print(filtered_grades)
