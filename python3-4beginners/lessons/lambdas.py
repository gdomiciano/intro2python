numbers = [1,2,3,4,5,6]

#Conventional way:
def square(n):
  return n*n

squared_list = list(map(square, numbers))
print(squared_list)


#lambda:
squared_list = list(map(lambda n: n*n, numbers))
print(squared_list)
