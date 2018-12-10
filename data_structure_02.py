#Tuple is same as list. define Tuple as x = (1, 2, 3)
print("-------------------------------------------------------------------")
items = (1, 2,  3, 4, 5,  [6,   7, 8, 9, 10], ("apple", "mango"))

print ("items = ", items)

for i in  items:
    print(i , type(i));

print("-------------------------------------------------------------------")
print("Now we will see some example of set")
print("-------------------------------------------------------------------")

A = set("Bangladesh")

print("set('Bangladesh') = ", A)

print("-------------------------------------------------------------------")
A = {1, 2, 3, 4, 5}
print("A = ", A)

B = {2, 4, 6, 8}
print("B = ", B)

c = A & B
print("A & B = ", c)

c = A | B
print("A | B = ", c)

c = A ^ B
print("A ^ B = ", c)

c = A - B
print ("A - B = ", c)

c = B - A
print("B - A = ", c)
print("-------------------------------------------------------------------")
