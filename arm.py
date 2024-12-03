#armstrong number
q=123
x=q
c=0
seq=0
while(x>0):
    c=c+1
    x=x//10
y=q
while(y>0):
    s=y%10
    seq=seq+s**c
    y=y//10  
if(seq==q):
    print("number is armstrong")
else:
    print("number is not armstrong")