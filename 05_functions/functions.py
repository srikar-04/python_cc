# returning square of a number

def square(num):     # These are technically called parameters
    return num*num

# print(square(int(input('Enter a number to see its square : '))))

def greet(name = 'srikar'): # Learn to add default value
    if (name.strip() == ''):
        name = 'srikar'
        return 'Hello ' + name + '!'
    return 'Hello ' + name + '!'

print(greet(''))

# CREATING A LAMBDA FUNCTION : 

# -->> lambda functions won't have any name. Just like callbacks in js

cube = lambda x: x**3  # lamda function for cubing a value

print(cube(3))

# Taking multiple arguments : 
def sum_all(*args):  # this is used for taking multiple arguments and we can write any name here instead of args
    # this "args" is nothing but a "tuple". so we can iterate on it
    # return sum(args) -->> returning sum using the default method
    print(args)     # Iterating over the tuple
    for i in args:
        print(i**2)

sum_all(1,2,3,4)
print(sum_all(1,2,3,4,5,6,7))

# Taking a key-value pair args 
def print_kwargs(**kwargs):
    for name, power in kwargs.items():
        print(f"{name}:{power}")

print_kwargs(name = 'batman', power = 'tech')
print_kwargs(name='spiderman', power='web', enemy='Dr.Octo')

# "Yeild" using generator functions : 

# yeild keyword makes a function as a generator, which allows it to produce a sequence of values lazily, one at a time, instead of computing them all at once.
def even_generator(limit):  
    for i in range(2, limit + 1, 2):
        yield i

for num in even_generator(10):
    print(num)