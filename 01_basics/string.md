# String In Python

## String Methods

- ### len()
    BASIC AS FUCK
    - returns the length
    ```python
    my_str = 'lemon tea'
    print(len(my_str)) # 9
    ```
- ### format()
    - formats the string, works like "dollar and braces" in js
    ```python
    chai_type = 'masala'
    count = 2
    order = 'I ordered {} cups of {} chai'
    # '{}' are called placeholders
    print(order.format(count, chai_type)) # 'I ordered 2 cups of masala chai'
    ```
- ### upper(), lower(), title(), capitalize()
    - changing the case of words
    ```python
    my_string = 'hello world!'
    print(my_string.upper()) # HELLO WORLD!
    print(my_string.lower()) # hello world!
    print(my_string.title()) # Hello World!
    print(my_string.capitalize()) # Hello world!
    ```
- ### strip()
    - trimming white spaces, same like .trim() in js
- ### split(char)
    - splits the string and converts it to array
    ```python
    fruits = 'banana, apple, grapes, kiwi'
    print(fruits.split(", ")) # ['banana', 'apple', 'grapes', 'kiwi']
    ```
- ### join(str)
    - converts array to string
    ```python
    my_arr = ['python', 'is', 'awesome']
    print(" ".join(my_arr)) # 'python is awesome'
    ```
- ## string splice
    - splicing or getting a part of string. Remember, strings are immutable, original string will never change
    ```python
    new_str = 'Hello World!'
    print(new_str[0:6]) # Hello -> last index is "not inclusive"
    print(new_str[:]) # Hello World! -> splices entire string
    print(new_str[2:]) # llo World! -> starts with the given index and goes till the end
    print(new_str[:6]) # Hello -> if first param is not given then it starts with 0th one
    print(new_str[0:6:2]) # Heo -> every 2nd char is picked after splicing (simply one char is skipped after splicing)
    print(new_str[0:6:3]) # Hl -> every 3rd char is picked after splicing (two chars are skipped after splicing)

    # GOTTA STUDY ABOUT FUCKING NEGITIVE INDEX AS 3RD PARAM
    ```
- ### find(str) & index(str)
    - returns the index at which the given string starts
    - returns the index of the string. 
    - The difference between find() and index() method is, find returns -1 if the word or char is not found. It does not throw any error. index throws error if the char or string is not present
- ## replace(oldChar, newChar)
    - we can replace a char or a string iteself
    ```python
    my_sentence = 'i love java'
    my_str = 'banana'
    print(my_sentece.replace('java', 'python')) # i love python
    print(my_str.replace('a', 'x')) # bxnxnx (replaces a with x)
    ```
- ### startsWith(string) & endsWith(string)
    - returns true or false
- ### count(string)
    - below is the example
    ```python
        fruit = 'banana'
        fruit.count('a') # returns 3
        fruit.count('an') # returns 2
    ```
- ## special cases
    - if we are using quotes inside quotes then we may face some problems. so we can either use '\' or 'r' literal which shows that it is a raw string literal
    ```python
    compliment = "He Said "Masala Chai Is Awesome"" # this will not be appropriate and will give us error

    # using back-slash
    compliment = "He Said \"Masala Chai Is Awesome\"" # Now this is treated as a complete string

    # using "r" literal for other things
    compliment_without_literal = "chai\ncode"
    compliment_with_literal = r"chai\ncode"
    print(compliment_wihtout_literal) # prints chai and code in seperate lines
    # chai
    # code
    print(compliment_with_literal) # prints the exact string
    # chai\ncode

    ## THIS WILL BE USEFUL WHILE DEFINING OR USING WINDOWS PATH, BECAUSE WINDOWS PAHT USES "\" 
    ```