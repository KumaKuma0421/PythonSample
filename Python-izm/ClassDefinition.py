# -----------------------------------------------------------------------------
class TestClass:

    def __init__(self):
        """ constructor
        デフォルトコンストラクタ
        """
        self.num1 = -1
        self.num2 = -1

    def setup(self, num1, num2):
        """setup(self, num1, num2)
        This is a function 'setup()'
        """
        self.num1 = num1
        self.num2 = num2

    def response(self):
        """response()
        This is a function 'response()'
        """
        return (self.num1, self.num2)


class TestExtendClass(TestClass):

    def __init__(self):
        super().__init__()
        self.num3 = -1

    def setup(self, num1, num2, num3):
        super().setup(num1, num2)
        self.num3 = num3

    def response(self):
        return (self.num1, self.num2, self.num3)


if __name__ == "__main__":

    testClass = TestClass()
    print("===== Class =====")
    num1 = testClass.num1
    num2 = testClass.num2
    print(testClass.response())

    print(testClass.setup.__doc__)
    print(testClass.response.__doc__)

    testClass.setup(0, 0)
    print(testClass.response())

    testExtendClass = TestExtendClass()
    print("===== TestExtendClass =====")
    num1 = testExtendClass.num1
    num2 = testExtendClass.num2
    num3 = testExtendClass.num3

    testExtendClass.setup(1, 1, 1)
    print(testExtendClass.response())
