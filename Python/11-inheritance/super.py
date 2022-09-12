class A:
    var1 = "i am var 1"
    def __init__(self):
        self.classvar1="i am classvar1 in class A"
        self.special="i am special"
    
class B(A):
    var2 = "i am var 2"
    def __init__(self):
        super().__init__()
        self.classvar1="i am classvar1 in class B"

obj1 = B()
print(obj1.special)
print(obj1.classvar1)