# In Java functions are not an object but in Python every function is an object

def getName():   # This funcion gets stored in a memory (<function getName at 0x0000012DA4963E20>)
    print("Hello")
print(getName) # getName is an object stored in the memory, here in the heap memory
               # internally this is a callable function __call__ (dunder method or magic method or special method)
               # Python memory management means, it internally uses the cpython