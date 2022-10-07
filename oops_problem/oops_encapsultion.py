class Base:
    def __init__(self):
        self.a = "Accessable"
        self.__c = "Attributerror"


class Derived(Base):
    def __init__(self):

        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


if __name__ == "__main__":
    obj1 = Base()
    print(obj1.a)
