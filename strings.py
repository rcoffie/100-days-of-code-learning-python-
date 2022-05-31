#out putting a code in python 
print('hello world')

#seeting  varible 
message = 'Hello World'
print(message)

#len function 
#The len() function returns the number of items in an object
print(len(message))

#Printing individual Characters in a string 
print(message[1])
# NB in programming charcter counting starts from 0, so this will output e 

#Accessing a range or characters  example accessing just (hello)
print(message[0:5])
#this is going to start counting from h which is the first letter and end at o which is the last lettter starting from 0 t0 5 . the first character is unclusive and the lat charcter is not 

#printing all characters into lowercase 

print(message.lower())

#printing characters in uppercase 

print(message.upper())

#using the count method 
print(message.count('llo'))

#using find 
print(message.find('World'))

# using replace method 

message = message.replace('World', 'Universe')
print(message)

#concatenating strings 

greeting = 'Hello'
name   = 'Michael'

message = greeting + ',' + name + ', Welcome!'
print(message)

#formating strings 

message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

#using f strings to fomat strings 

message = f'{greeting}, {name} . Welcome!'

print(message)

print(dir(message))
print(help(str))

print(help(str.lower()))