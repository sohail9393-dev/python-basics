print("hello world")
#it prints hello world

character_name = "John"
character_age = "35"
print(f"there once was a man named {character_name} he was {character_age} years old. ")
# This script uses f-strings to insert a character's name and age into a sentence.

print("giraffe\nacademy")
# This prints "giraffe academy" on two lines using the newline character \n

phrase= "giraffe academy"
print(phrase)
# This stores a string in a variable and prints it to the screen

print(phrase+" is good")
# This adds another string to the existing phrase and prints the combined result

print(phrase.upper())
# This converts the phrase to uppercase letters and prints it

print(phrase.lower())
# This converts the phrase to lowercase letters and prints it

print(phrase.isupper())
# This checks if all characters in the phrase are uppercase and prints the result (True or False)

print(phrase.islower())
# This checks if all characters in the phrase are lowercase and prints the result (True or False)

print(phrase.upper().isupper())
# This converts the phrase to uppercase, then checks if all characters are uppercase and prints the result

print(phrase.lower().islower())# This converts the phrase to lowercase, then checks if all characters are lowercase and prints the result

print(len(phrase))
# This prints the length of the phrase (number of characters)

print(phrase[0])# This prints the character at index 0 of the phrase (the first character)

print(phrase.index("g"))
# This finds the index of the first occurrence of the letter "g" in the phrase and prints it

print(phrase.replace("giraffe","elephant"))
# This replaces "giraffe" with "elephant" in the phrase and prints the modified phrase

print(2+2)
# This prints the result of adding 2 to 2

print(10%3)
# This prints the remainder when 10 is divided by 3

my_num=5
print(str(my_num))
# This converts the number to a string so it can be printed or combined with other strings

print(f"{my_num} is my fav no.")
# This uses an f-string to insert the value of my_num into the sentence

print(pow(4,3))
# This calculates 4 raised to the power of 3 and prints the result

print(max(4,6))
# This prints the larger of the two numbers

print(min(4,6))
# This prints the smaller of the two numbers

print(round(3.2))
# This rounds the number to the nearest integer and prints it

from math import *
# This imports all functions from the math module

print(floor(3.7))
# This rounds the number down to the nearest integer and prints it

print(ceil(3.7))
# This rounds the number up to the nearest integer and prints it

print(sqrt(36))
# This calculates the square root of 36 and prints the result


Name = input("Enter your name")
Age = input("Enter your age")

print(f"hello {Name}, you are {Age} years old")
# This program takes the user's name and age as input, then prints a personalized greeting using an f-string

num1= input("Enter a number")
num2= input("Enter another number")
result= int(num1)+int(num2)
print(result)
# This program takes two numbers as input, converts them to integers, adds them, and prints the result

num1= input("Enter a number")
num2= input("Enter another number")
result= float(num1)+float(num2)
print(result)
# This program takes two numbers as input, converts them to floating-point numbers, adds them, and prints the result
# float is a number with a decimal point

# CREATING A GAME

color= input("Enter a color")
plural_noun= input("Enter a plural_noun")
celeb= input("Enter a celeb")
print(f"Roses are {color}")
print(f"{plural_noun} are blue")
print(f"I hate {celeb}")
# This is a simple mad libs game that asks the user for a color, a plural noun, and a celebrity name,
# then uses those inputs to generate a funny poem using f-strings.


#LISTS

friends=["Kevin","Karen","Jim","Oscar","Toby"]
print(friends)
# This creates a list of friends and prints it
print(friends[1:3])
print(friends)
# This adds two new elements to the end of the friends list and prints the updated list

friends.append("Stanley")
print(friends)
# This adds a single new element to the end of the friends list and prints the updated list

friends.insert(1,"Kelly")
print(friends)
# This inserts "Kelly" at index 1 in the friends list and prints the updated list

friends.remove("Jim")
print(friends)
# This removes "Jim" from the friends list and prints the updated list

# friends.clear()
# print(friends)
# This would remove all elements from the friends list, making it empty

friends.pop()
print(friends)
# This removes the last element from the friends list and prints the updated list

print(friends.index("Kevin"))
# This finds the index of "Kevin" in the friends list and prints it

print(friends.count("Kevin"))
# This counts how many times "Kevin" appears in the friends list and prints the result

friends.sort()
print(friends)
# This sorts the friends list alphabetically and prints it

lucky_numbers=[4,8,15,16,23,42]
lucky_numbers.sort()
print(lucky_numbers)
# This sorts the lucky_numbers list numerically and prints it

lucky_numbers.reverse()
print(lucky_numbers)
# This reverses the order of elements in the lucky_numbers list and prints it

friends2=friends.copy()
print(friends2)
# This creates a copy of the friends list and assigns it to friends2, then prints friends2

print(set(friends))
# A set stores unique, unordered values and removes duplicates automatically

lucky_numbers= [2,4,11,2,3]
friends.extend(lucky_numbers)
print(friends)
# This adds all the elements from lucky_numbers to the end of the friends list using the extend() method

# FUNCTIONS

def say_hi():
    print("hello user")
say_hi()    
# This defines a function that prints a greeting and then calls the function to display it

def say_hi(name,age):
    print(f"hello {name}, you are {age}")
say_hi("sohail",25)
# This defines a function that prints a greeting and then calls the function to display it
say_hi("sohail",25)
say_hi("rehman",23)
# Calling a function again

def cube(num):
    return num*num*num
print(cube(3))
# This defines a function that calculates the cube of a number and returns the result


# IF STATEMENTS

is_male=True
if is_male:
    print("you are a male")
else:
    print("you are not a male")
# This checks if the user is male using a boolean variable and prints a message accordingly

is_male=False
if is_male:
    print("you are a male")
else:
    print("you are not a male")
# This checks if the user is male using a boolean variable and prints a message accordingly

# IF STATEMENTS AND COMPARISIONS

def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(300,40,5))
# This function takes three numbers and returns the maximum using conditional statements

# CALCULATOR

num1=float(input("Enter first number"))
num2=float(input("Enter second number"))
op=input("Enter operator")
    
if op=="+":
        print(num1+num2)
elif op=="-":
        print(num1-num2)
elif op=="*":
        print(num1*num2)
elif op=="/":
        print(num1/num2)

else:
        print("invalid operator")


# WHILE LOOP

i=1
while i<=10:
     print (i)
     i+=1
print("done with loop")      
# This loop prints numbers from 1 to 10 using a while loop


# Guess game of Loop
secret_word="clock"
guess=""
while guess!= secret_word:
     guess=input("Enter guess")
print("you win")     
# This code runs a guessing game that keeps asking the user to guess the secret word until they get it right


# Guessing Game
secret_word="key"
guess=""
guess_count=0
guess_limit=3
out_of_guesses=False
while guess!= secret_word and not(out_of_guesses):
    if guess_count<guess_limit:
        guess=input("Enter guess")
    guess_count+=1
else:
    out_of_guesses=True
# A simple word guessing game.
# The program keeps asking the user to guess the secret word until they get it right.
# Once the correct word is entered, it prints "you win".


# FOR LOOP
friends=["Jim","Karen","Kevin"]
for friend in friends:
    print(friend)

friends=["Jim","Karen","Kevin"]
for index in range(len(friends)):
    print([index])
# Prints each index of the friends list wrapped in square brackets


friends=["Jim","Karen","Kevin"]
for index in range(len(friends)):
    print(friends[index])       
# Prints each friend's name from the list using their index

for index in range(5):
    if index==0:
        print("first iteration")
    else:
         print("not first")
# This loop runs 5 times. It checks if it's the first iteration and prints a special message for it; otherwise, it prints "not first".

def raise_to_power(base_num,pow_num):
    result=1
    for index in range(pow_num):
        result=result*base_num
    return result
print(raise_to_power(2,3))

# 2D LISTS AND NESTED LOOPS

num_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]]
print(num_grid[2][1])
# Access and print the element in the 3rd row and 2nd column (value: 8)

num_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]]
for row in num_grid:
    for col in row:
        print(col)
# Loop through each row and then each column to print every number in the 2D list

num_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]]
for row in num_grid:
        print(row)
# Loop through each row in the 2D list and print the entire row

employees_file = open("workers.txt", "r")
# Open the file "workers.txt" in read mode ("r")
print(employees_file.read())
# Read the entire contents of the file and print it to the console
employees_file.close()
# Close the file to release system resources

employees_file = open("workers.txt", "a")
employees_file.write("\nNew worker added")
employees_file.close()



        











