# Control Flow Statements

langs = ['Shift','DSA','Python']
for lang in langs:
    print(lang)
    print('------')
print("Last Statement")
print("----------------------------------")

language = 'PYTHON'
for x in language:
    print(x)
print("----------------------------------")

for i in range(0,5):
    print(i)
print("----------------------------------")

langs = ['Shift','DSA','Java','Python']
for lang in langs:
   if lang == 'Java':
       break
   print(lang)
print("----------------------------------")

langs = ['Shift','DSA','Java','Python']
for lang in langs:
   if lang == 'Java':
       continue
   print(lang)
print("----------------------------------")

methods = ['Electric','Petrol','Diesel']
behaviour = ['BMW','Audi','Brezza','XUV500']
for att in methods:
    for beh in behaviour:
        print(att,beh)
    print("------")
print("----------------------------------")

for i in range(0,10):
    print("Data Structures and Algorithms...")
print("----------------------------------")

number = 1
while number < 6:
    print(number)
    number = number + 1
print("----------------------------------")

number = int(input("Enter the number you would like:"))
while number != 5:
    print(f"Your desired number is {number}.")
    number = int(input("Enter the number you would like:"))
print("Thank you for leaving..")
print("----------------------------------")

"""age = 15
while age <=17:
    print("You cannot vote, you must be a major..")"""

"""age = 30
while True:
    print("You can vote, you are old enough..")"""

for i in range(10):
    if i == 5:
        break
    print(i)
print("----------------------------------")

for i in range(10):
    if i == 5:
        continue
    print(i)
print("----------------------------------")

y = 25
if y>25:
    pass
print("Hello world..")

y = 25
if y>25:
    #WRITE ANYTHING
 print("Hello world..")
