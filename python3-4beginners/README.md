# Python 3 Tutorial for Beginners
https://www.youtube.com/playlist?list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK


## Notes - lessons 3 to 5:

### Numbers
> type() - check the type of a element(object)
> len() - check the length of a element(object)

**return a float**
```python
>>> 5/5.
1.0
```

**return a Integer**
```python
>>> 5 // 5
1

Brackets
I???
Division
Multiplication
Adition
Subtraction

### Strings
>>> greet = 'hello'
```

**get char in a string from left to right**
```python
>>> greet[0]
'h'
```

**get char in a string from right to left**
```python
>>> greet[-1]
'o'
```

**slice a string first parameter is inclusive, necond is non-inclusive , can be from positive to negative, ne**the other way around-->
>>> greet[0:4]
'hell'
```

**check length in general**
len(greet)
5


### lists```

**concatenate lists**
```python
>>> fib1 = [1,1,2,3,5,8,13]
>>> fib2=[21,34,55]
>>> fib1+fib2
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

**update one item inside a list**

>>> fib1[0] = 9
>>> fib1
[9, 1, 2, 3, 5, 8, 13]
```

**Add a item to a list**

>>> fib
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
>>> fib.append(89)
>>> fib
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

**remove the last item from a list**
```python
>>> fib.pop()
89
>>> fib
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

**remove the first item that contains the value**
```python
>>> fib.remove(89)
>>> fib
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

**remove a item based on a specific index(es)**
```python
>>> del(fib[10])
>>> del(fib[4:6])
>>> fib
[1, 1, 2, 3, 13, 21, 34, 55]
```

**Create nested lists**
```python
>>> nums = [mix, fib, [1,2,3,4]]
>>> nums
[['hi', 'blue', 'plate', 25], [1, 1, 2, 3, 13, 21, 34, 55], [1, 2, 3, 4]]
```

**Access nested lists**
```python
>>> nums[1][5]
21

