#!/bin/python

# Numeric variables - hold integers and decimal values
age = 25
temperature = 98.6

# String variables - Stores a sequence of characters enclosed in single or double quotes
name = "John Doe"
message = 'Hello, world!'

# Boolean variables - only hold the values true and false
is_true = True
is_false = False

# List variables - Stores a collection of items, which can be of different types.
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']

# Tuple variables
coordinates = (10, 20)

# Dictionary variables
person = {'name': 'Alice', 'age': 30}

# Set variables
unique_numbers = {1, 2, 3}

# None variable
empty_value = None

# area do retangulo
lenght = 45
width = 76
area = print(lenght * width)
print=(area)

# area do circulo 
pi = 3.14
radius = 8.9
# pi * radius ao quadrado 
area = print(pi * (radius ** 2))
print = area

# concatenating strings 
x = "hello"
y = "world"
print(x + " " + y) 

# importante Strings e inteiros não se falam

# tamanho da string utilizando len
txt = "NumeroTres"
len_strig = len(txt)
print(len_strig)

# trazendo indexes de strings
# um index sempre começa com zero
word = "programming"
print(word[2])
print(word[1])

# substituição de letras em strings (ou frases inteiras)
word = "Ocygen"
word_new = word.replace('c', 'x')
print(word_new)

# trabalhando com substring 
str = 'Interesting'
substring = str[0:4]
print(substring)

var = "String"
substring = var[2:]
print(substring)

# using input and converting to integer, if no converted th number will be a string
num = int(input())
print(num)

# mini calculator
a = int(input())
b = int(input())
sum = int(a + b)
diff = int(a - b)
print(sum)
print(diff)