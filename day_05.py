## loops

## for loops  indention is important
# fruits = ['apple','banana','grapes']    ### remember here the test variable we are searching key in fruits 
# for test in fruits:
#     print(test)
#     print(test + 'cat')   ## here we adding values inside the loop if we have added outside then the loop will not print this statment
#     print(fruits) ## if we see here we added value in loop it printed 3 times
# print(fruits)  ## if we see here we actualyy printed outside of loop that is why it printed once


## average height

# studentheight = input("please enter your student height \n ")
# print(type(studentheight))
# height = studentheight.split(', ')
# print(height)
# testlenght = len(height)
# print(type(testlenght))

# total = int(height[0]) + int(height[1]) + int(height[2]) + int(height[3])
# print(total)
# avg = round(total / testlenght)
# print(avg)


# student = ('12, 13, 14, 15')
# print(len(student))   ## doesn't know what is the problem for this output coming 14



##same problem with sum and len

# student_height = [12,13,14]
# print(sum(student_height))


## same problem with for loop
# student_height = [12,13,14,15]
# total_height = 0
# for height in student_height:
#     total_height += height
#     print(total_height)
# print(type (total_height))
# lengths = len(student_height)
# print(type(lengths))

# avg = round (total_height / lengths)
# print(avg)
# value = round(total_height / avg)
# print(value)


#  it is different here adding using sum function
# student_heights = [180, 124, 165, 173, 189, 169, 146]
# print(sum(student_heights))




## height score finding from list

# student_scores = [ 91, 64, 89, 86]
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f'the highest score is {highest_score}')


## height weight

# weight = [25, 45, 35, 36, 38]
# myweight = 0
# for heighest_weight in weight:
#     if heighest_weight > myweight:
#         myweight = heighest_weight
# print(f'my highest weight is {myweight}')

## for loop with range function

# total = 0
# for numbers in range (1, 101):
#     total += numbers
# print(total)


## print sum of even numbers from 1 to 100 
# total = 0
# for evennumbers in range(2, 101, 2):
#     total += evennumbers 
# print(total)



## fizz buzz program

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print('fizzbuzz')
#     elif number % 3 == 0:
#         print('fizz')
#     elif number % 5 == 0:
#         print('fizz')
#     else:
#         print(number)


## password generator program


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# letter_req = int(input("how many letters req \n "))
# numbers_req = int(input('how many numbers req \n '))
# symbols_req = int(input('how many symbols req \n '))

# password = ""

# for char in range(1, letter_req + 1):
#     password += random.choice(letters)
# for char in range (1, numbers_req + 1):
#     password += random.choice(numbers)
# for char in range (1, symbols_req + 1):
#     password += random.choice(symbols)
# print(password)


## Hard level Password Generator


print("Welcome to the PyPassword Generator!")
letter_req = int(input("how many letters req \n "))
numbers_req = int(input('how many numbers req \n '))
symbols_req = int(input('how many symbols req \n '))

password_list = []

for char in range(1, letter_req + 1):
    password_list.append(random.choice(letters))
for char in range (1, numbers_req + 1):
    password_list.append(random.choice(numbers))
for char in range (1, symbols_req + 1):
    password_list.append(random.choice(symbols))
#print(password_list)

random.shuffle(password_list)
#print(password_list)

password = ""

for char in password_list:
    password += char
print(f"your password is {password}")



