#Write a program to print the Fibonacci series using for loop ... 1234
a=0
b=1
n=int(input("enter a num : "))
print(a)
print(b)
for i in range(3,n):
    c=a+b
    print(c)         
    a=b 
    b=c 

    