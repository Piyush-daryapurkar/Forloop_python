#Write a program to reverse a number 
#c=int(input("enter a num : "))

c=1234
x=c
rev=0
rem=0#1234
while(x>0):
    rem=x%10
    rev=rem
    x=x//10
    print(rev,end="")
print()
print(c)
if(rev==c):
    print("palindrome")
else:
    print("NOT")
