class A:
    def __init__(self):
        print("Im from A")

class B(A):
    def __init__(self):
        print("Im from B")
        super().__init__()

class C(B):
    def __init__(self):
        print("Im from C")
        super().__init__()

print(C())