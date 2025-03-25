# List in python (Mutable)

## slicing and appending of list :
- same like strings we can also splice lists
#### slicing :
```python
chai_varities = ["lemon", "black", "oolong", "ginger", "mint"]
print(chai_varities[1:4]) # ['black', 'oolong', 'ginger']
# after splicing, the result will also be an array
# can do all different splicing techniques, like hopping and all(3rd param), just like in strings
print(chai_varities[1:]) # ['black', 'oolong', 'ginger', 'mint']
```
#### slicing and replacing multiple elements : 
- we can slice multiple elements from the list like shown above and can replace it
```python
chai_varities = ["lemon", "black", "oolong", "ginger", "mint"]
chai_varities[1:2] = ['elaichi'] # this will replace 'black' ith lemon. But here the question is why we have added []

# if we do not write string inside a list, the string iteself is treated like a list of characters. so 'black' will be replaced with 'e', 'l', 'a', 'i', 'c', 'h', 'i'

# the best part is we can replace multiple items of list

chai_varities[1:3] = ['elaichi']

# now both ['black', 'oolong'] list is replaced with 'elaichi'
``` 
#### Adding items to list :
- we can append any element at the end of list or we can insert the element at particualr index
```python
chai_varities = ["lemon", "black", "oolong", "ginger"]
chai_varities.append('white') # adds 'white' at the end of the list

chai_varities.insert(1, 'white') # inserts 'white' at 1st index (before 'black')

# we can also append a list to a list using extend
# Best part is we can append any iterable items like dictionaries and tuples to the list using extend() function

list_1 = ['apple', 'banana']
list_2 = ['grapes', 'kiwi']
tuple_1 = ('oranges', 'watermelon')

print(list_1.extend(list_2)) # result will be a lis containing both list's elements "stored in list_1"

print(list_1.extend(tuple_1)) # same working as above
```
## Removing list items : 
- pop(), remove() are the methods used
```python
chai_varities = ["lemon", "black", "oolong", "ginger"]
print(chai_varities.pop()) # 'returns' last element in list and 'modifies' the list because lists are mutable

print(chai_varities.remove('black')) # removes black from list but 'does not return anything'

# -->> If there is more than one occurance of the specified string, then remove() only removes the first occurance <<--

# -->> for removing multiple items we should use 'list comprehension' in python. List comprehension is used in many other ways also <<--

```
#### List Comprehension : 
```python
my_list = [1, 2, 3, 3, 2, 4, 2]
value_to_remove = 2
my_list = [x for x in my_list if x!== value_to_remove] # this removes all 2s from list

my_nums = [x**2 for x in range(10)] # calculates the power of 2 for all numbers in the range of 0 to 10 (10 is non inclusive)
```