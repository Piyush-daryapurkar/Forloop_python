#Write a program to check whether a number is prime or not ...
x=int(input("enter num : "))
for i in range(1,x+1):
    c=0
    for j in range(1,i+1):#17
        if(i%j==0):
            c=c+1

    if(c==2):
        print(i,"prime")