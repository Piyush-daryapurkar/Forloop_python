# Write a program to find the factorial of a number 
x=int(input("enter num : "))
fact=1
z=1
while (0<x):
    z=x
    fact=fact*z
    print(z,"*",end="")
    x=x-1
print("fac is",fact)