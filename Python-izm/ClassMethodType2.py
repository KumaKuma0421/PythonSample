class TestVariable1:

    index = -1
    message = "uninitialized."
    messageList = {}  # ここで初期化すると、クラス変数の振舞になる。

    def __init__(self):
        self.index = 0
        self.message = "initialized."

    def set_message(self, index, value):
        self.index = index
        self.message = value
        self.messageList["index"] = self.index
        self.messageList["message"] = self.message

    def get_message(self):
        return (self.index, self.message, self.messageList)


print("-"*40)
test1 = TestVariable1()
test1.set_message(1, "New Value 1")

test2 = TestVariable1()
test2.set_message(2, "New Value 2")

print(test1.get_message())
print(test2.get_message())


class TestVariable2:

    index = -1
    message = "uninitialized."
    messageList = None

    def __init__(self):
        self.index = 0
        self.message = "initialized."
        self.messageList = {} # ここで初期化することで、インスタンス変数になる。

    def set_message(self, index, value):
        self.index = index
        self.message = value
        self.messageList["index"] = self.index
        self.messageList["message"] = self.message

    def get_message(self):
        return (self.index, self.message, self.messageList)


print("-"*40)
test3 = TestVariable2()
test3.set_message(3, "New Value 3")

test4 = TestVariable2()
test4.set_message(4, "New Value 4")

print(test3.get_message())
print(test4.get_message())
