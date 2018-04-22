num1 = 3.1425467389
num2 = 10.2903948

#previous
print('PREVIOUS:')
print('num1 is', num1, 'and num2 is', num2)

#FORMAT METHOD
print('\nFORMAT METHOD:')
print('num1 is {0} and num2 is {1}'.format(num1, num2))
#show only 3 digits
print('num1 is {0:.3} and num2 is {1:.3}'.format(num1, num2))
#show only 3 decimal points
print('num1 is {0:.3f} and num2 is {1:.3f}'.format(num1, num2))


#USING F-STRING
print('\nF-STRING:')
print(f'num1 is {num1} and num2 is {num2}')
#show only 3 digits
print(f'num1 is {num1:.3} and num2 is {num2:.3}')
#show only 3 decimal points
print(f'num1 is {num1:.3f} and num2 is {num2:.3f}')
