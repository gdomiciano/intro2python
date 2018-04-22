from random import shuffle

def jumble(word):
  anagram = list(word)
  shuffle(anagram)
  return ''.join(anagram)

words = ['beetroot', 'carrots', 'potatoes']
anagrams = []

#For method
for word in words:
  anagrams.append(jumble(word))
print(anagrams)

#Map method
anagrams = list(map(jumble, words))
print(anagrams)

#list comprehension method
anagrams = [jumble(word) for word in words]
print(anagrams)
