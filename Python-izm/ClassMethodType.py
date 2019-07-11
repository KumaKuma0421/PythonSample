#
# メソッドの種類
#

class TestClass:
    _counter1: int = -1
    counter2: int = -1

    # インスタンスメソッド
    def sample_method(self, param1: int):
        self._counter1 += param1
        self.counter2 += param1
        print("This is a instance method 'sample_method' param1 is " + str(param1))

    # クラスメソッド
    @classmethod
    def sample_class_method(cls, param1: int):
        cls._counter1 += param1
        cls.counter2 += param1
        print("This is a class method 'sample_class_method' param1 is " + str(param1))

    # スタティックメソッド
    @staticmethod
    def sample_static_method(param1, param2):
        _counter1 += (param1 + param2)
        counter2 += param1
        print("This is a static method 'sample_static_method' sum is " +
              str(param1 + param2))


testObj = TestClass()

print("instance function.")
testObj.sample_method(1)
message = "_counter1 = {0} counter2 = {1}".format(
    testObj._counter1, testObj.counter2)
print(message)
testObj.sample_method(2)
message = "_counter1 = {0} counter2 = {1}".format(
    testObj._counter1, testObj.counter2)
print(message)
print("=" * 20)

testObj = TestClass()

print("class function at instance.")
testObj.sample_class_method(1)
message = "_counter1 = {0} counter2 = {1}".format(
    testObj._counter1, testObj.counter2)
print(message)
testObj.sample_class_method(2)
message = "_counter1 = {0} counter2 = {1}".format(
    testObj._counter1, testObj.counter2)
print(message)
print("-" * 20)

print("class function on demand.")
TestClass.sample_class_method(3)
message = "_counter1 = {0} counter2 = {1}".format(
    testObj._counter1, testObj.counter2)
print(message)
TestClass.sample_class_method(4)
message = "_counter1 = {0} counter2 = {1}".format(
    testObj._counter1, testObj.counter2)
print(message)
print("=" * 20)

# print("static function")
# testObj.sample_static_method(1, 2)
# TestClass.sample_static_method(2, 3)
