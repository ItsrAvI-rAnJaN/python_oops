class Car:

    attr1 = "Machine"

    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    Ford = Car("Ford")
    Ferrari = Car("Ferrari")

    print("Ford is a {}".format(Ford.__class__.attr1))
    print("Ferrari is also a {}".format(Ferrari.__class__.attr1))

    print("\nMy Car name is {}".format(Ford.name))
    print("My Car name is {}".format(Ferrari.name))
