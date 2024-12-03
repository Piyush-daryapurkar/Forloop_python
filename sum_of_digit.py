# Write a program to find the sum of digits of a number 
# Input: 12345
# Output: 15
x=int(input("enter a number : "))
sum=0
rev=0
while(x>0):
    rev=x%10
    sum=sum+rev
    x=x//10
print(sum)  