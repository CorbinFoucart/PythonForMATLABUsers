import numpy as np

# declaring functions
def increment(x):
    """ increments argument passed in
    docstring here -- comments
    @param x the thing to be incremented
    """
    return x + 1
    #x = x+1 # fine, but verbose
    #x++     # not fine -- not supported

def increment_list(_list):
    #for _item, val in enumerate(_list):
    #    _list[_item] += 1
    _list[0] + 1

def return_two_things():
    return 0, 1

def increment_both(x, optional=None):
    """ optional keywords """
    if optional is not None:
        optional += 1
    x += 1
    return x, optional

#a = 1
#b = increment(a)
#print(b)
#print(a)
#a = increment(a)
#print(a)

#my_list = [20, 40]
#increment_list(my_list)
#print(my_list)
#for idx, _ in enumerate(my_list):
#    print(idx)
#
#x, _ = return_two_things()
#print(x)

print(increment_both(0, optional=1))
print(increment_both(0))
#print(increment_both(0, 1))

#increment_list(my_list)
#print(my_list)
