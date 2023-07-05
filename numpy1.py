import numpy as np


# to make 1-dimensional array

print( np.arange(10) )
print( np.arange(20) )

print ( np.arange(2, 3, 0.1)  )
print ( np.arange(2, 20, 0.4)  )


# this function convert into 
#   (  X ,   X,     x )
#      |     |      |
#  start    end     |
#       \-----/--->eqivalent halfs

print( np.linspace(1., 4., 6) )
print( np.linspace(1., 11., 3) )






       
# to make 1-dimensional array

# defauld 1 value crates In , n belonges to Natual numbers
print( np.eye(3) )
print( np.eye(2) )
print( np.eye(4) )

# 2 values create no.of rows and columns

print( np.eye(3, 5) )
print( np.eye(4, 2) )
print( np.eye(3, 2) )


# creates diagonal matrics
print(np.diag([1, 4, 7]))
print(np.diag([29, 12, 6]))

print(np.diag([1, 2, 3], 1))

print(np.diag([1, 2, 3], 0))

print(np.diag([1, 2, 3], 2))

print(np.diag([1, 2, 3], -1))

print(  np.diag( np.array([[1, 2], [3, 4]]) ) )
print(  np.diag( np.array([[1, 2,3], [4,5,6],[7,8,9]]) ) )






