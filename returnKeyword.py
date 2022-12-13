# x = 4

# if x ==3:
#     return x #error: "return" can be used only within a function

def getAge(age):
    # print(age)
    age=age+7
    return age
print(getAge(25)) #We always need to print statement when you're calling the function to display the value

def getAger(age):
    age=age+2
    return age
    age=age+8 #this line doesn't get executed because anything line after the return statement is not considered 
print(getAger(15))

def getAgerr(age):
    age=age+2
    return # It will not return anything expect the keyword None or if you dont want to return anything then return None
    age=age+8 
print(getAgerr(15))

def retx(age):
    age=age+2
    return 13
    return 14 # This doesn't get executed as it is not like assignment operators & python recognizes line by line
print(retx(5))