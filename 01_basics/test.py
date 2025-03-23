def print_string(string):
    print(string)

print_string('hello world')

chai_one = 'lemon tea'
chai_two = 'ginger tea'
chai_three = 'masala chai'
chai_four = 'black tea'

# we have to reload the file after adding anything new. So we have imported the importlib module
# from importlib import reload
# reload(test) => reloads the file

# NOTES : 

# 1. dir() is a method which is used to list all the attributes like variables, functions etc. Below is the example
# username = "srikar"
# print(dir(username)) ---> ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# 2. We can explore all the attributes that a string have
# 3. Numbers and strings are not collected immideately by garbage collector because python works agressively on numbers and strings. So they are collected a little late compared to others

# UNDERSTANDING MUTABLE AND IMMUTABLE IN DEAPTH : 
 
# l1 = [1,2,3]
# l2  = l1
# In the above case both l1 and l2 will point to the same list and if any value change in l1 will also appear in l2
 
# l1 = [1,2,3]
# l2 = l1[:]
# In the above case a copy of l1 is created and l2 is pointing to the copy. So any change in l1 will not affect l2
# we used "slice" here to copy, we can also use "copy()" module