'''for i in range(1,5):
    for j in range(1,8):
        if j>=5-i and j<=3+i:
            print("*",end="")
        else:
            print("",end="")    
    print(" ")

 
for i in range(1,5):
    for j in range(1,8):
        if j>=5-i and j<=3+i:
            print("*",end="")
            
        else:
            print("",end="")    
    print(" ") 

i=0
a="santabanta"
while i< len(a):
    if (a[i]=="n"):
       break
    i=i+1
print("cuurent letter : ",a[i])
print("position of alphabet is : ",i)


i=1
while i<6:
    i+=1
    if i==3:
        continue
    print(i)'''


for i in range(1,11):
    if i%3==0:
        continue
    else:
        print(i)