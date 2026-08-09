
#Data Types and Functions

num1 = 5
print(num1, 'is of type', type(num1))

num2 = 8.3
print(num2, 'is of type', type(num2))

string = "Hansini"
print(string, 'is of type', type(string))
print("-----------------------------------------------")

num1 = int(2.3)
print(num1)

num2 = int(-25.6)
print(num2)

num3 = float(25)
print(num3)

num4 = complex('6+2j')
print(num4)
print("-----------------------------------------------")

ages = [50, 28,549,]
print(ages)
print("-----------------------------------------------")

student = ['Jack', 32, 'Computer Science', [2,8]]
print(student)

empty_list = []
print(empty_list)
print("-----------------------------------------------")

lang = ['Python', 'HTML', 'Java', 'DSA', 'DBMS', 'C']

print("Language = ", lang[1])
print("Language = ", lang[3])
print("-----------------------------------------------")

lang = ['Python', 'HTML', 'Java', 'DSA', 'DBMS', 'C']

print("Language = ", lang[-2])
print("Language = ", lang[-4])
print("-----------------------------------------------")

list = ['P', 'R', 'O', 'G', 'R', 'A', 'M']

print("List =", list)
print("List[2: 5] =", list[2: 5])    
print("List[2: -2] =", list[2: -2])  
print("List[0: 3] =", list[0: 3])
print("-----------------------------------------------")

list = ['P', 'R', 'O', 'G', 'R', 'A', 'M']

print("List =", list)
print("List[5:] =", list[5:])    
print("List[ :-2] =", list[ : -2])  
print("List[ : ] =", list[ : ])
print("-----------------------------------------------")

fruits = ['Apple', 'Banana', 'Orange']
print('Original List:', fruits)

fruits.append('Cherry')
print('Updated List:', fruits)
print("-----------------------------------------------")

fruits = ['Apple', 'Banana', 'Orange']
print('Original List:', fruits)

fruits.insert(0, 'Cherry')
print('Updated List:', fruits)
print("-----------------------------------------------")

numbers = [1, 3, 5]
print('Numbers:', numbers)

even_numbers  = [2, 4, 6]
print('Even numbers:', even_numbers)

numbers.extend(even_numbers)
print('Updated Numbers:', numbers)
print("-----------------------------------------------")

colors = ['Red', 'Black', 'Mint Green']

print('Original List:', colors)

colors[0] = 'Purple'
colors[2] = 'Teal Blue'

print('Updated List:', colors)
print("-----------------------------------------------")

numbers = [2, 4, 5, 31, 17, 30, 25]
numbers.remove(31)
print(numbers)
print("-----------------------------------------------")

names = ['John', 'Eva', 'Laura', 'Nick', 'Jack']

del names[1]
print(names)

del names[1: 3]
print(names)

print("-----------------------------------------------")

cars = ['BMW', 'Mercedes', 'Audi']
print('Length of the List:', len(cars))
print("-----------------------------------------------")

fruits = ['Apple', 'Banana', 'Cherry', 'Orange']
for fruit in fruits:
    print(fruit)
print("-----------------------------------------------")

fruits = ['Apple', 'Banana', 'Orange']
for fruit in fruits:
    print(fruits)
print("-----------------------------------------------")

numbers = (6, 2, -5)
print(numbers)
print("-----------------------------------------------")


lang = ('Python', 'HTML', 'Java', 'DSA', 'DBMS', 'C')

print("Language = ", lang[1])
print("Language = ", lang[3])
print("-----------------------------------------------")

cars = ['BMW', 'Mercedes', 'Audi']
cars[0] = 'Nissan'
print(cars)
print("-----------------------------------------------")

fruits = ('Apple', 'Banana', 'Orange')
for fruit in fruits:
    print(fruit)
print("-----------------------------------------------")

name = "Data Stuctures and Algorithms"
print(name)
print("-----------------------------------------------")

message = 'Data Stuctures and Algorithms using Python.'
print(message)
print("-----------------------------------------------")

greet = 'AMRITA VISHWA VIDYAPEETHAM'

print(greet[7]) 
print(greet[-16]) 
print(greet[7:13])
print(greet[7:])
print("-----------------------------------------------")

message = 'Hola Amigos'
message = 'Hello Friends'
print(message);
print("-----------------------------------------------")

message = '''
Never gonna give you up,
Nor gonna let you down
'''
print(message)
print("-----------------------------------------------")

str1 = "Amaravathi, Campus!"
str2 ="Coimbathore."
str3 ="Amaravathi, Campus!"

print(str1 == str2)
print(str1 == str3)
print("-----------------------------------------------")

greet = "Hansini "
name = "Sarora"

result = greet + name
print(result)
print("-----------------------------------------------")

greet = 'AMRITA'
for letter in greet:
    print(letter)
print("-----------------------------------------------")

greet = 'AMRITA'
for letter in greet:
    print(greet)
print("-----------------------------------------------")

greet = 'SECOND YEARS'
print(len(greet))
print("-----------------------------------------------")

print('a' not in 'Program')
print('at' in 'Battle')
print("-----------------------------------------------")

example = "He said, \"What's there?\""
print(example)
