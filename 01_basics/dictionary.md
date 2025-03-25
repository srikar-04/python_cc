# Dictionary in python : 
## Decleration, getting and modifying values : 
```python
chai_types = {"Masala":"Spicy", "Ginger": "Zesty", "Green":"Mild"}
# we can get the value in two types

print(chai_types['Masala']) # 'Spicy'
# this list like syntax gives us error when there is no such thing called 'Masala' in the dictionay

print(chai_types.get('Masala')) # 'Spicy'
# this .get() method will not throw any error if there is no matched key

# Modifying values :

chai_types["Green"] = "Refreshing" # now the value of Green will not be mild, it will be Refreshing
```
#### looping over dictionaries : 
```python
chai_types = {"Masala":"Spicy", "Ginger": "Zesty", "Green":"Mild"}

for(chai in chai_types): 
    print(chai, chai_types[chai])
    # these will return key-value paris because 'chai' contains all the 'keys'
    
    # Masala Spicy
    # Ginger Zesty 
    # Green Mild

# we can define direct key-value pairs while writing for loop

for key,value in chai_types.items():
    # this is the syntax to get key, value pairs
```
- we can also use len() function for dictionaries
- .popitem() is used to pop the last 'element'
- can also use .copy() method
- .clear() removes all the items from the dictionary and the dictionary will be empty

WATCH YT CC VIDEO FOR BETTER UNDERSTANDING AND MORE INFO