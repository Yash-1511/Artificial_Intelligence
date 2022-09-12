import random
uppercase = "QWERTYUIOPLKJHGFDSAZXCVBNM"
lowercase = "qwertyuioplkjhgfdsazxcvbnm"
number= "0123456789"
symbols = "@#!%&*(){<}>"
add = uppercase+lowercase+number+symbols
length=16
password = "".join(random.sample(add,length))
print(password)