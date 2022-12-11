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