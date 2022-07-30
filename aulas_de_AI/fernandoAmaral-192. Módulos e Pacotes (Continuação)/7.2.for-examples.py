# https://stackoverflow.com/questions/18294534/is-there-a-foreach-function-in-python-3
"""
def foreach(fn,iterable):
    for x in iterable:
        fn(x)
// Python
for val in array:
    print(val)
    
So, yes, there is a "foreach" in python. It's called "for".

What you're describing is an "array map" function. 
This could be done with list comprehensions in python:
"""
names = ['tom', 'john', 'simon']

#namesCapitalized = [capitalize(n) for n in names]

"""
Other examples:

1. Python Foreach Loop:
"""

array1 = ['bmw', 'renegade', 'cerato', 'auto-drive']
for value in array1:
    print(value)
    # a
    # b

# 2.Python For Loop:

array2 = ['algoritmo', 'booleano', 'ibm', 'apple', 'asus', 'dell']
for index in range(len(array2)):
    print("index: %s | value: %s" % (index, array2[index]))
    # index: 0 | value: a
    # index: 1 | value: b


"""
bmw
renegade
cerato
auto-drive
index: 0 | value: algoritmo
index: 1 | value: booleano
index: 2 | value: ibm
index: 3 | value: apple
index: 4 | value: asus
index: 5 | value: dell
"""
