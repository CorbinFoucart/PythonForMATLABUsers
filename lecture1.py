import numpy as np

# printing to console
print('meow')

# matlab-like zeros, numpy array
z = np.zeros(3)

# python list
my_list = [2, 4, 'banana']
for _item in my_list:
    print(_item)

# FOR LOOPS
# matlab
# for i=1:3
#     z(i) = i
# end
#
# python equivalent, indexing into lists/arr
for i in range(3):
    z[i] = i

for elm in range(1,4,2):
    print(elm)

# matlab linspace
a = np.linspace(0, 10, 5)

# declare arrays of differing types
print(np.zeros(10))
print(np.zeros(10, dtype=int))
print(np.zeros(10, dtype=bool))

# declaring functions
# importing local files

