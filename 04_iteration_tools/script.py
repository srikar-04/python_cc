# import time

# print('time is :', time.time())
# username  = 'srikar'
# print('username is :', username)

# Memory-efficient generator
def create_squares(n):
    for x in range(1, n):
        yield x*x

# Generator only creates values when needed
squares = create_squares(1000000)

for square in squares:  # __next__() is called automatically.
    print(square)

# print(squares.__next__())
