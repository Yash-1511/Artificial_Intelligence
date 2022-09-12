from abc import ABCMeta,abstractmethod
class Base(metaclass=ABCMeta):
    @abstractmethod
    def greet(self):
        return 0
class derived(Base):
    def greet(self):
        print("Hello user")

obj1 = derived()
obj1.greet()
#we cannot create object of abstract base class