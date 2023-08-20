### functions


# def greet():
#     print('hey you started learning functions')
#     print('let start using functions')

# greet()


### functions with INPUT

# def greet_name(name):
#     print(f"hey {name}, how are you doing")

# greet_name("eliyaz")



### functions with multiple input

# def greet_multiple(name,place):
#     print(f"hello {name}")
#     print(f"hey which is town {place}")

# #greet_multiple("tomcat","anantapur")

# greet_multiple(name='eliyaz',place='sep')



#### area calculation challenge

# test_h = int(input("please type height of your wall : \n "))
# test_w = int(input("please type width of your wall: \n "))
# area = (test_h * test_w)/5
# total_cans = round(area)
# print(f"the total cans required is {total_cans}")

# import math
# def paint_cal(height, width, cover):
#     area = height * width
#     number_of_cans = math.ceil(area / cover)

# print(f'you will need this many cans {number_of_cans}')

# test_h = int(input("please type height of your wall : \n "))
# test_w = int(input("please type width of your wall: \n "))
# coverage = 5
# paint_cal(height=test_h,width=test_w,cover=coverage)


####### prime number checking


# def prime_number(number):
#     for i in range (2, number):
#         if number % i == 0:
#             print("not a prime")
#         else:
#             print("it is a prime")

# test = int(input("please type your number \n "))
# prime_number(number=test)


##### caesar program

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
       position =  alphabet.index(letter)
       new_position = position + shift_amount
       new_letter = alphabet[new_position]
       cipher_text += new_letter
    print(f"the actual output is {cipher_text}")

#encrypt(plain_text=text, shift_amount=shift)

def decrypt(cipher_test, shift_amount):
    plain_text = ""
    for letter in cipher_test:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"the actual output is {plain_text}")

# decrypt(cipher_test=text, shift_amount=shift)

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_test=text, shift_amount=shift)

