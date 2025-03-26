# calculating positive number

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_number_count = 0

for number in numbers:
    if number > 0:
        positive_number_count += 1

print('No of positive numbers in the list : ',positive_number_count)

# calculating even number to a given number 'n'

n = int(input('Enter a number to find all even numbers in that range : '))

even_numbers_list = []

for number in range(1, n+1):
    if number % 2 == 0:
        even_numbers_list.append(number)

print('list of even numbers in the given range : ', even_numbers_list)

# Reversing a string using loop

original_string = 'python'
reversed_string = ''

for char in original_string:
    reversed_string = char + reversed_string

print('This is the reversed string : ', reversed_string)

# Finding first non-repeated character in a string (DSA days, long time no seeee)

input_string = 'teeter'

non_repeated_char = ''

# count = 0

# for first_char in input_string:
#     count = 0
#     index = input_string.index(first_char)
#     # print('inside first loop')
#     if(index == len(input_string) - 1):
#         non_repeated_char = first_char
#         break
#     for second_char in input_string[index+1:]:
#         # print('inside second loop')
#         if(first_char == second_char):
#             count = count + 1
#     if count == 0:
#         non_repeated_char = first_char
#         break

# print('first non repeated character is :', non_repeated_char)

# -->> this is the simple solution

for char in input_string:
    if input_string.count(char) == 1:
        non_repeated_char = char
        break

print('first non repeated character is :', non_repeated_char)