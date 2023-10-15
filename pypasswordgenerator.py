# Password Generator Project.
import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+','?','_','-','^','@','.','/','|','~']
#word = ''

print('---&&----^^----...Welcome To My PyPassword Generator!..---@@----**---###---\n')
nr_letters = int(input('How many letters would you like to be in your password?\n'))
nr_symbols = int(input('How many symbols do you want to be in your password?\n'))
nr_numbers = int(input('How many numbers would you like to be in your password?\n'))
#nr_word = str(input('Enter a secret word to include in your password\n'))

#Eazy level
# fgh^*23

#Hard level
#g^2jk8&

# This is the eazy level
# password = ''

# for char in range(1,nr_letters +1):
#     password += random.choice(letters)

# for char in range(1,nr_numbers+1):
#     password += random.choice(numbers)

# for char in range(1,nr_symbols+1):
#     password += random.choice(symbols)        

# print(password)    

# This is the hard level
password_list = []

for char in range(1,nr_letters +1):
    password_list.append(random.choice(letters))

for char in range(1,nr_numbers+1):
    password_list += random.choice(numbers)

for char in range(1,nr_symbols+1):
    password_list += random.choice(symbols)        

print(password_list) 
random.shuffle(password_list)
print(password_list)
 
password = '' 
for char in password_list: 
    password += char
print(f'Your password is: {password}')    
num_password = len(password)
print(f'Your password has {num_password} characters')