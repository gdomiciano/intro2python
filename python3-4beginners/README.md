# Python 3 Tutorial for Beginners
https://www.youtube.com/playlist?list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK


## Notes - lessons 3 to 5:

> type() - check the type of a element(object)
> len() - check the length of a element(object)
> set() - does not show duplicated values from a object, however does not put it in order
> sorted() - sort elements in numerical or alphabetical order (first it sorts capital letters and then lower case):
```python
>>> sorted(names)
['Amora', 'Geisy', 'ariana', 'geisy', 'luna', 'melina', 'raquel']
```

### Numbers
**return a float**
```python
>>> 5/5.
1.0
```

**return a Integer**
```python
>>> 5 // 5
1

<!-- Brackets
I???
Division
Multiplication
Adition
Subtraction -->

```

### Strings
`>>> greet = 'hello'`

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

**slice a string first parameter is inclusive, necond is non-inclusive , can be from positive to negative, not in the other way around**
```python
>>> greet[0:4]
'hell'
```

**check length in general**
```python
>>> len(greet)
5
```

### Lists

**concatenate lists**
```python
>>> fib1 = [1,1,2,3,5,8,13]
>>> fib2=[21,34,55]
>>> fib1+fib2
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

**update one item inside a list**
```python
>>> fib1[0] = 9
>>> fib1
[9, 1, 2, 3, 5, 8, 13]
```

**Add a item to a list**
```python
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
```

### Dictionaries

**declaration**
```python
ninja_belts = {"crystal":"red", "ryu": "black"}
#or
person = dict(name='Geisy', age=25, height="168cm")
```

**Access a value through a key**
```python
>>> person['name']
'Geisy'
```

**Access dict keys/values:**
```python
>>> person.keys()
dict_keys(['name', 'age', 'height'])

>>> person.values()
dict_values(['Geisy', 25, '168cm'])
```

**Create a list with keys/values**
```python
>>> list(person.keys())
['name', 'age', 'height']
>>> list(person.values())
['Geisy', 25, '168cm']
```

**count inside a dict**
```python
>>> vals = list(person.values())
>>> vals.count(25)
1
```

**add a item in a dict**
```python
>>> person['weight'] = 54
>>> person
{'name': 'Geisy', 'age': 25, 'height': '168cm', 'weight': 54}
```
