def Iterable(cls):
    """ Decorator to make a class iterable. """

    def __iter__(self):
        return iter(
            (
                self.__dict__[attr]
                for attr in dir(self)
                if not callable(getattr(self, attr)) and not attr.startswith("__")
            )
        )

    setattr(cls, "__iter__", __iter__)
    return cls


if __name__ == "__main__":
    """ Example code. """

    def test_print(obj):
        print("[START] *** Test ouput ***")
        print(*obj)
        for member in obj:
            print(member)

    @Iterable
    class IterTest:
        def __init__(self):
            self.member1 = 1
            self.member2 = "one"
            self.member4 = object()
            self.member5 = None

        def resetMembers(self, member1, member2, member3, member4, member5):
            self.member1 = member1
            self.member2 = member2
            self.member3 = member3
            self.member4 = member4
            self.member5 = member5

        def copyCtr(self, iterTest):
            self.resetMembers(*iterTest)

    testInstance = IterTest()
    test_print(testInstance)

    testInstance2 = IterTest()
    testInstance2.resetMembers(1, 2, 3, 4, 5)
    test_print(testInstance2)

    testInstance.copyCtr(testInstance2)
    test_print(testInstance)
