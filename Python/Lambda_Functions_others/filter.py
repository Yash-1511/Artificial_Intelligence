def trueoffalse(num):
    if num>3:
        return True
    else:
        return False

l = [1,2,3,4,5,6]
print(list(filter(trueoffalse,l)))