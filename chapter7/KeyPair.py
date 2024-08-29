class KeyPair():
    def __init__(self, value, number = 1):
        self.value = value
        self.number = number

    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value  < other.value
    
    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value <= other.value
    
    def __ge__(self, other):
        return self.value >= other.value

    def __ne__(self, other):
        return self.value != other.value