print("Enter the value of a:")
a = int(input())
print("Enter the value of b:")
b = int(input())
print("Enter the value of c:")
c = int(input())
if a > b:
    if a > c:
        print("a is larger")
else:
    if b > c:
        print ("b is largest")
    else:
        print("c is largest")
