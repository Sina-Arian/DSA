from Stack import Stack
from Queue import Queue

def palindromeTester(inWord):
    stack = Stack()
    queue = Queue()
    readyWord = caring(inWord)
    for ch in readyWord:
        stack.push(ch)
        queue.inqueue(ch)

    return(palindrome(stack, queue))


def caring(inWord):
    lowered = inWord.lower()
    out = []
    for ch in lowered:
        if ch not in "'?!:;,. ":
            out.append(ch)
    return out


def palindrome(stack, queue):
    if stack.size() != queue.size():
        return False
    else:
        while stack.size() != 0:
            if stack.pop() != queue.dequeue():
                return False
    return True

def main():
    inStr = input("Enter the string:\n")
    res = palindromeTester(inStr)
    if res is True:
        print("it's a palindrom")
    else:
        print("it's not a palindrom")

if __name__ == '__main__':
    main()