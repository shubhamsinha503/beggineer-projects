text = input("enter the inputed text : ")

if("subscribe this" in text):
    spam = True
elif("make more money " in text):
    spam = True
elif("make a lot of money" in text):
    spam= True
else :
    spam = False
    
    
if(spam==False):
    print("your email is spam less")
else :
    print("it is a spam")                    