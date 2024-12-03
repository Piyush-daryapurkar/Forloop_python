'''for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
        
    print("")


for i in range(6):
    print("a",end="")
    for j in range(6):
        print("b",end="")
    print("")


for i in range(1,6):
    for j in range(1,6):
        print("*",end="")
    print("")    




for i in range(1,6):
    for j in range(1,6):
        if(j<=i):
            print("*",end="")
        else:
            print("",end="")    
    print("")  




for i in range(1,6):
    for j in range(1,6):
        if(j>=i):
            print("*",end="")
        else:
            print("",end="")    
    print("") '''  


for i in range(1,6):
    for j in range(1,6):
        if(j<=6-i):
            print("*",end="")
        else:
            print("",end="")    
    print("")                  