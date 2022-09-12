def mulwith10(n):
    return n*10
l = [1,2,3]
#method 1
# l2=[]
# for i in l:
#     l2.append(mulwith10(i))
# print(l2)
#method 2
print(list(map(mulwith10,l)))