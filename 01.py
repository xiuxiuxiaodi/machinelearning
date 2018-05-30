class Counter:
    def __init__(self):
        self.counter = 0  # 这里会触发 __setattr__ 调用

    def __setattr__(self, name, value):
        super().__setattr__(name, value)




    def __delattr__(self, name):
        self.counter -= 1
        super().__delattr__(name)

a = Counter()
a.counter=3
print (a.counter)
print("word")