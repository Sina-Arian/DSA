from Stack import Stack

def parenBalance2(s: str):
    stack = Stack()
    for ch in s:
        if ch in '([{':
            stack.push(ch)
        elif ch in ')]}':
            if stack.size() == 0:
                return False
            else:
                opener = stack.pop()
                if opener+ch not in ['()', '[]', r'{}']:
                    return False

    return stack.size() == 0
