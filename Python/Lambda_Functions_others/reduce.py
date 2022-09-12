from functools import reduce
add = lambda a,b:a+b
l = [1,2,3,4]
print(reduce(add,l))