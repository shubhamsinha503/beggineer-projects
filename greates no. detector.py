num1= int(input("enter a number 1 : "))
num2= int(input("enter a number 2 : "))
num3= int(input("enter a number 3 : "))
num4= int(input("enter a number 4 : "))

if(num1>num2):
    f1= num1
else:
    f1=num2
    
    
if(num3>num4):
    f2=num3
else:
    f2=num4
    
f1 = str(f1)
f2= str(f2)    
if(f1>f2):
    print(f1 + "  is the greatest") 
else:
    print(f2 + "  is the greates")                   

