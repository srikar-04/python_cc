# Different methods for opening a file

# method 1

file = open('test.txt', 'w') # 'w' specifies that we are opening the file in write mode

# if we donot have any such file then it will create a new file, because we have specified write mode

try:
    file.write('Hello World')
finally:
    file.close() 

# method 2

with open('test.txt', 'w') as file:   # this syntax will automatically close the file
    file.write('Hello World')