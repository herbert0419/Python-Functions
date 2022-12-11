# There are 4 types of functional params/args

# 1. Positional length Args/Required Args
# 2. Default Args
# 3. Variable length args (*) or vargs
# 4. keyword length args (**) or kwargs


# 1. name & age are positional arguments or the required arguments
# Error if any postitional args not given : TypeError: person() missing 1 required positional argument: 'age'

def person(name,age):
    print('Person Details:')
    print(name)
    print(age)
person('Soumyadeep',19)

# 2. country is default parameter here

def person(name,age,country='USA'):
    print(name)
    print(age)
    print(country)

person('Soumyadeep',19,'India') # Here we overwrite the country with the default args of USA with India
# Default argument never comes before the Non-Default arguments/Positional Args
# Default params should be pushed to last

# 3. *locations (Suppose you live in India, but to mention states * is used, like inplace of the default args)
    #  * location is a vargs here or variable args
def person(name,age,country='IN',*location):
    print(name)
    print(age)
    print(country)
    print(location)

person('Shaan',18,'Raj','WB','MH')

# To get a more clear idea about this, check the function below:

def getEmployee(*empName):
    print(empName)

getEmployee('Rakesh','Mukesh','Harry') # Here we got the 3 employee name at once without passing 3 positional args instead of caling function 3 times.
                                       # This is the main function for the * or vargs (variable length args)
                                       # Data is taken in the form of a Tuple (* indicates the tuple, basically we dont want to modify the data)

# Also, 

# def getEmployee(empName):
#     print(empName)
# getEmployee('Rakesh','Mukesh','Harry') # Throws error: TypeError: getEmployee() takes 1 positional argument but 3 were given

# 4. kwargs (**) - Keyword args

def employee(name,age,*location,**worklocation):
    print(name)
    print(age)
    print(location)
    print(worklocation)

employee('Shaan',24,'TX','WD','NY',winter='Boston',summer='San Fransisco')

# if noticed: the *vargs gives tuple as output whereas **kwargs gives dictionary as output.
# Always keep in mind that the Positional/Non-Default Params should be written first, default at the last, vargs/kwargs in the middle (*vargs,default args,**kwargs)
# Basically the Keywords are the variable only passed in the form of kwargs