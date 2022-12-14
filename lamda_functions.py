# Anonymus functions in Python is known as the lambda function
# Lambda is a Keyword : deals with shorthand logic, save memory
# Syntax: 
    # lambda variables:expression

print(lambda x:x*2) # Gives output -- <function <lambda> at 0x000001484D633E20>
                    # 0x000001484D633E20 - is the memory location of the function address

def a(x):return x*34
print(a(3)) # passing the x value here for the lambda function (lambda x:x*34)

add_numbers = lambda x,y:x+y
print(add_numbers(4,8))

add_ext = lambda x,y=4:x+y
print(add_ext(7))

take_list = lambda x:len(x)
print(take_list([1,2,3]))

take_string = lambda name:name.upper()
print(take_string('shaan')) 

take_str_op = lambda name: (name.upper(),len(name)) # while writing multiple data type one time, use tuple or else it will throw error
print(take_str_op('shobhan'))

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# find the sum of squares of even numbers
# Steps: 
        # filter -- even --->map --(square) -->reduce(sum)

# IIFE: Immediately invoke function expression

print((lambda x:x+3)(2)) # Short hand Script

# Technically: 
a = lambda x:x+3
print(a(3)) # passing the x value explicitly

print((lambda x,y:x+y)(4,5)) # adding two numbers using iffe