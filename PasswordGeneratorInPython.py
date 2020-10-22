####################################################################################################################
# 
# Author: GRISHMA BAJRACHARYA 
# 
# About the program: This program gets user's input for required number of Uppercase Alphabets, Digits and
# Special Characters for the password. The program then calculates the remaining space for Lowercase Alphabets.
# Then, it randomly chooses digits, special characters, lowercase and uppercase alphabets, shuffles them and 
# generates a password. I imported python libraries: 'random' and 'string' to complete this project.
# 
# All the user inputs are validated using while loop and try & except. User inputs will loop indefinitely till the 
# user enters a valid input.
# 
# When the sum of number of uppercase alphabets, digits and special characters is greater than length of password,
# then it gives an error message and loops all the way to the top asking the user to input again.
#
####################################################################################################################

# Import libraries
import datetime
import getpass
import random
import string

# Welcome message
print('WELCOME TO THE PASSWORD GENERATOR!')
print()
username = getpass.getuser()
print('Your Username is : ', username, '  &  ', 'Today is :', (datetime.date.today()))
print()

# Declaring variables
UPPERCASEALPHABET = string.ascii_uppercase
LOWERCASEALPHABET = string.ascii_lowercase
SPECIAL_CHARACTERS = string.punctuation
NUMBERS = string.digits

while True:

    # Validating User Input for Length of password
    while True:
        try:
            lengthofpassword = int(input ('STEP 1: Please enter a number between 8 & 16 for password length : '))
                    
            while lengthofpassword < 8 or lengthofpassword > 16:
                print()
                print ('    Error! Length of password must be between 8 and 16.')
                print()
                lengthofpassword = int(input ('STEP 1: Please enter a number between 8 & 16 for password length : '))
        
            break

        except Exception as e:
            print()
            print ('    You have an error!', e)
            print()
            continue

    # Validating User Input for Number of Uppercase Alphabets
    while True:
        try:
            numOfUppercase = int(input ('STEP 2: How many Uppercase Alphabets do you want? (0 - 3) : '))
                    
            while numOfUppercase < 0 or numOfUppercase > 3:
                print()
                print ('    Error! Number of Uppercase Alphabets must be between 0 and 3.')
                print()
                numOfUppercase = int(input ('STEP 2: How many Uppercase Alphabets do you want? (0 - 3) : '))
        
            break

        except Exception as e:
            print()
            print ('    You have an error!', e)
            print()
            continue

    # Validating User Input for Number of Special Characters
    while True:
        try:
            numOfSpecialCharacters = int(input ('STEP 3: How many special characters do you want? (0 - 3) : '))
                    
            while numOfSpecialCharacters < 0 or numOfSpecialCharacters > 3:
                print()
                print ('    Error! Number of special characters must be between 0 and 3.')
                print()
                numOfSpecialCharacters = int(input ('STEP 3: How many special characters do you want? (0 - 3) : '))
        
            break

        except Exception as e:
            print()
            print ('    You have an error!', e)
            print()
            continue

    # Validating User Input for Number of Digits
    while True:
        try:
            numOfNumbers = int(input ('STEP 4: How many numbers do you want? (0 - 3) : '))
                    
            while numOfNumbers < 0 or numOfNumbers > 3:
                print()
                print ('    Error! Number of digits must be between 0 and 3.')
                print()
                numOfNumbers = int(input ('STEP 4: How many digits do you want? (0 - 3) : '))
        
            break

        except Exception as e:
            print()
            print ('    You have an error!', e)
            print()
            continue
            
    try:    
        # Calculating remaining number of Lowercase Alphabet 
        numOfLowercase = lengthofpassword - numOfSpecialCharacters - numOfNumbers - numOfUppercase
        numOfLowercase = int(numOfLowercase)

        # Generating password
        uppercasePw = random.sample(UPPERCASEALPHABET, numOfUppercase)
        lowercasePw = random.sample(LOWERCASEALPHABET, numOfLowercase)
        numPw = random.sample(NUMBERS, numOfNumbers)
        specialCharPw = random.sample(SPECIAL_CHARACTERS, numOfSpecialCharacters)
        
        tempPassword = uppercasePw + lowercasePw + numPw + specialCharPw
        password = random.shuffle(tempPassword)
        password = ''.join(tempPassword)
        print()
        print('YOUR PASSWORD IS:', password,
              '\nThank you!'
              '\n')
        break

    # Error if length of password < sum of inputs (number of Uppercase alphabets, digits and special characters)
    except Exception as e:
        print('\n'
              '\n    You have an error!', e,
              '\n    Please try again.'
              '\n')
        continue