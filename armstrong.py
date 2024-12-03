n=int(input("enter a num : "))
x=n
a=(n%10)
n=(n//10)
b=(n%10)
n=(n//10)
s=n*n*n+b*b*b+a*a*a
print(s)
if(x==s):
    print("ARMSTRONG")
else:
    print("NOT ARMSTRONG")